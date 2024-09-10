import boto3, json

print("\n----A basic call to the Converse API----\n")

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

message_list = []

initial_message = {
    "role": "user",
    "content": [
        { "text": "How are you today?" } 
    ],
}

message_list.append(initial_message)

response = bedrock.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

response_message = response['output']['message']

print(json.dumps(response_message, indent=4))

#
print("\n----Alternating user and assistant messages----\n")

message_list.append(response_message)
print(json.dumps(message_list, indent=4))

#
print("\n----Including an image in a message----\n")

with open("image.webp", "rb") as image_file:
    image_bytes = image_file.read()

image_message = {
    "role": "user",
    "content": [
        { "text": "Image 1:" },
        {
            "image": {
                "format": "webp",
                "source": {
                    "bytes": image_bytes #no base64 encoding required!
                }
            }
        },
        { "text": "Please describe the image." }
    ],
}

message_list.append(image_message)

response = bedrock.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4))

message_list.append(response_message)


#
print("\n----Setting a system prompt----\n")

summary_message = {
    "role": "user",
    "content": [
        { "text": "Can you please summarize our conversation so far?" } 
    ],
}

message_list.append(summary_message)

response = bedrock.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=message_list,
    system=[
        { "text": "Please respond to all requests in the style of a pirate." }
    ],
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4))

message_list.append(response_message)

#
print("\n----Getting response metadata and token counts----\n")

print("Stop Reason:", response['stopReason'])
print("Usage:", json.dumps(response['usage'], indent=4))

