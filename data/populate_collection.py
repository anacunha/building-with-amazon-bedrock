import boto3, json
import chromadb
from chromadb.utils.embedding_functions import AmazonBedrockEmbeddingFunction

#startup script to populate vector db

def get_text_embeddings_collection(collection_name):
    session = boto3.Session()
    embedding_function = AmazonBedrockEmbeddingFunction(session=session, model_name="amazon.titan-embed-text-v2:0")
    
    client = chromadb.PersistentClient()
    index = client.get_or_create_collection(collection_name, embedding_function=embedding_function)
    
    return index


def initialize_collection(collection_name, source_json_file):
    
    collection = get_text_embeddings_collection(collection_name)
    
    if collection.count() == 0:
        
        row_count = 0
        
        with open(source_json_file) as json_file:
            source_json = json.load(json_file)
            
            for item in source_json:
                row_count = row_count + 1
                collection.add(
                    ids=[str(item['id'])],
                    documents=[item['document']],
                    metadatas=[item['metadata']],
                    embeddings=[item['embedding']]
                )
    
    print(f"Initialized collection {collection_name}")
    
    return collection



initialize_collection('services_collection', 'services_with_embeddings.json')

initialize_collection('bedrock_faqs_collection', 'bedrock_faqs_with_embeddings.json')

