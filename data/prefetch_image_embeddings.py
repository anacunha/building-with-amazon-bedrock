import boto3, json, base64, os


#calls Amazon Bedrock to get a vector from either an image, text, or both
def get_multimodal_vector(input_image_base64=None, input_text=None):
    
    session = boto3.Session()

    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    
    request_body = {}
    
    if input_text:
        request_body["inputText"] = input_text
        
    if input_image_base64:
        request_body["inputImage"] = input_image_base64
    
    body = json.dumps(request_body)
    
    response = bedrock.invoke_model(
    	body=body, 
    	modelId="amazon.titan-embed-image-v1", 
    	accept="application/json", 
    	contentType="application/json"
    )
    
    response_body = json.loads(response.get('body').read())
    
    embedding = response_body.get("embedding")
    
    return embedding


#creates a vector from a file
def get_vector_from_file(file_path):
    with open(file_path, "rb") as image_file:
        input_image_base64 = base64.b64encode(image_file.read()).decode('utf8')
    
    vector = get_multimodal_vector(input_image_base64 = input_image_base64)
    
    return vector


def serialize_image_embeddings():
    
    processed_items = []
    row_count = 0
    
    path = "../labs/image_search/images"
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        
        embedding = get_vector_from_file(file_path)
        
        row_count = row_count + 1
        print(f"Processing item: {row_count}")
        item_dict = {
            'id': str(row_count),
            'document': f"images/{file}",
            'metadata': {'file_path': f"images/{file}" },
            'embedding': embedding
        }
        
        processed_items.append(item_dict)
    
    
    with open('images_with_embeddings.json', 'w') as json_file:
        json.dump(processed_items, json_file)
    
    
    print("Saved images_with_embeddings.json to disk!")



serialize_image_embeddings()
