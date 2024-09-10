import boto3
import itertools
import chromadb
from chromadb.utils.embedding_functions import AmazonBedrockEmbeddingFunction

def get_text_embeddings_collection(collection_name):
    session = boto3.Session()
    embedding_function = AmazonBedrockEmbeddingFunction(session=session, model_name="amazon.titan-embed-text-v2:0")
    
    client = chromadb.PersistentClient()
    index = client.get_or_create_collection(collection_name, embedding_function=embedding_function)
    
    return index

def get_vector_search_results(collection, question):
    
    results = collection.query(
        query_texts=[question],
        n_results=4
    )
    
    return results
    
def get_similarity_search_results(collection_name, question):

    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    collection = get_text_embeddings_collection(collection_name)
    
    search_results = get_vector_search_results(collection, question)
    
    flattened_results_list = list(itertools.chain(*search_results['documents'])) #flatten the list of lists returned by chromadb
    
    print(f"\n{collection_name}\n")
    
    print(flattened_results_list)
    
    return flattened_results_list


get_similarity_search_results("services_collection", "Managed database service")


get_similarity_search_results("bedrock_faqs_collection", "What can I do with Bedrock agents?")


