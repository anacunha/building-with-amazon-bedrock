import boto3
from io import BytesIO


#get a BytesIO object from file bytes
def get_bytesio_from_bytes(image_bytes):
    image_io = BytesIO(image_bytes)
    return image_io

#load the bytes from a file on disk
def get_bytes_from_file(file_path):
    with open(file_path, "rb") as image_file:
        file_bytes = image_file.read()
    return file_bytes


#generate a response using Anthropic Claude
def get_response_from_model(prompt_content, image_bytes, mask_prompt=None):
    session = boto3.Session()
    
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    
    image_message = {
        "role": "user",
        "content": [
            { "text": "Image 1:" },
            {
                "image": {
                    "format": "jpeg", #this doesn't seem to matter
                    "source": {
                        "bytes": image_bytes #no base64 encoding required!
                    }
                }
            },
            { "text": prompt_content }
        ],
    }
    
    response = bedrock.converse(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        messages=[image_message],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0
        },
    )
    
    output = response['output']['message']['content'][0]['text']
    
    return output
