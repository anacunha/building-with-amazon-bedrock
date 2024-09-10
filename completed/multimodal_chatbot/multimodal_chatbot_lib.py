import boto3
from io import BytesIO

MAX_MESSAGES = 20

class ChatMessage(): #create a class that can store image and text messages
    def __init__(self, role, message_type, text, bytesio=None, image_bytes=None):
        self.role = role
        self.message_type = message_type
        self.text = text
        self.bytesio = bytesio #used for streamlit rendering
        self.image_bytes = image_bytes #used to pass to the model

#get a BytesIO object from file bytes
def get_bytesio_from_bytes(image_bytes):
    image_io = BytesIO(image_bytes)
    return image_io

#load the bytes from a file on disk
def get_bytes_from_file(file_path):
    with open(file_path, "rb") as image_file:
        file_bytes = image_file.read()
    return file_bytes


def convert_chat_messages_to_converse_api(chat_messages):
    
    messages = []
    
    for chat_msg in chat_messages:
        if (chat_msg.message_type == 'image'):
            messages.append({
                "role": "user",
                "content": [
                    {
                        "image": {
                            "format": "jpeg", #this doesn't seem to matter
                            "source": {
                                "bytes": chat_msg.image_bytes
                            }
                        }
                    }
                ]
            })
        else:
            messages.append({
                "role": chat_msg.role,
                "content": [
                    {
                        "text": chat_msg.text
                    }
                ]
            })
            
    return messages


def chat_with_model(message_history, new_text=None, new_image_bytes=None):
    session = boto3.Session()
    
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    
    if new_text:
        new_text_message = ChatMessage('user', 'text', text=new_text)
        message_history.append(new_text_message)
        
    elif new_image_bytes:
        image_bytesio = get_bytesio_from_bytes(new_image_bytes)
        new_image_message = ChatMessage('user', 'image', text=None, bytesio=image_bytesio, image_bytes=new_image_bytes)
        message_history.append(new_image_message)
    
    
    number_of_messages = len(message_history)
    
    if number_of_messages > MAX_MESSAGES:
        del message_history[0 : (number_of_messages - MAX_MESSAGES) * 2] #make sure we remove both the user and assistant responses
    
    
    messages = convert_chat_messages_to_converse_api(message_history)
    
    response = bedrock.converse(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        messages=messages,
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0,
            "topP": 0.9,
            "stopSequences": []
        },
    )
    
    output = response['output']['message']['content'][0]['text']
    
    response_message = ChatMessage('assistant', 'text', output)
    
    message_history.append(response_message)
    
    return

