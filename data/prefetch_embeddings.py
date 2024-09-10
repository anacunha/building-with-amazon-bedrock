import boto3, json

#Load directory/csv/json-process and store metadata, docs, ids, and embeddings


def get_text_embedding(text):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    
    response = bedrock.invoke_model(
        body=json.dumps({ "inputText": text }), 
        modelId="amazon.titan-embed-text-v2:0", 
        accept="application/json",
        contentType="application/json"
    )
    
    response_body = json.loads(response['body'].read())
    return response_body['embedding']
    

def serialize_services_embeddings():
    
    processed_items = []
    row_count = 0
    
    with open('services.json') as json_file: 
        services_json = json.load(json_file)
        
        for item in services_json:
            row_count = row_count + 1
            print(f"Processing item: {row_count}")
            item_dict = {
                'id': str(row_count),
                'document': item['description'],
                'metadata': {'name': item['name'], 'url': item['url'] },
                'embedding': get_text_embedding(item['description'])
            }
            
            processed_items.append(item_dict)
            
            #collection.add(
            #    ids=[str(row_count)],
            #    documents=[item['description']],
            #    metadatas=[{'name': item['name'], 'url': item['url'] }])
    
    with open('services_with_embeddings.json', 'w') as json_file:
        json.dump(processed_items, json_file)


    print("Saved services_with_embeddings.json to disk!")


def serialize_faqs_embeddings():
    
    processed_items = []
    row_count = 0
    
    #with open('services.json') as json_file: 
    with open('bedrock_faqs.json') as json_file:
        services_json = json.load(json_file)
        
        for item in services_json:
            row_count = row_count + 1
            print(f"Processing item: {row_count}")
            item_dict = {
                'id': str(row_count),
                'document': item['question'] + "\n" + item['answer'],
                'metadata': {'topic': 'bedrock' },
                'embedding': get_text_embedding(item['question'] + "\n" + item['answer'])
            }
            
            processed_items.append(item_dict)
            
            #collection.add(
            #    ids=[str(row_count)],
            #    documents=[item['description']],
            #    metadatas=[{'name': item['name'], 'url': item['url'] }])
    
    with open('bedrock_faqs_with_embeddings.json', 'w') as json_file:
        json.dump(processed_items, json_file)
    
    
    print("Saved bedrock_faqs_with_embeddings.json to disk!")


serialize_faqs_embeddings()

serialize_services_embeddings()
