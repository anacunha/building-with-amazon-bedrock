import boto3, json

################################################################

print("\n----Uma chamada básica para a Converse API----\n")

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

initial_message = {
    "role": "user",
    "content": [
        { "text": "Como você está hoje?" }
    ],
}

message_list = []
message_list.append(initial_message)

response = bedrock.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0,
    }
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4, ensure_ascii=False))

################################################################

print("\n----Alternando entre mensagens do usuário e do assistente----\n")

message_list.append(response_message)
print(json.dumps(message_list, indent=4, ensure_ascii=False))


################################################################

print("\n----Alternando entre mensagens do usuário e do assistente----\n")

with open("image.webp", "rb") as image_file:
    image_bytes = image_file.read()

image_message = {
    "role": "user",
    "content": [
        { "text": "Image 1:" },
        { "image": {
                "format": "webp",
                "source": {
                    "bytes": image_bytes
                }
            }
        },
        { "text": "Por favor, descreva a imagem."}
    ],
}

message_list.append(image_message)
response = bedrock.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0,
    }
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4, ensure_ascii=False))

message_list.append(response_message)

################################################################

print("\n----Configurando um prompt de sistema----\n")

summary_message = {
    "role": "user",
    "content": [
        { "text": "Você poderia resumir a conversa até agora?" }
    ],
}

message_list.append(summary_message)
response = bedrock.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0,
    },
    system=[
        { "text": "Por favor, responda a todos os pedidos no estilo de um pirata." }
    ]
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4, ensure_ascii=False))

message_list.append(response_message)

################################################################

print("\n----Obtendo metadados da resposta e contagens de tokens----\n")

print("Stop Reason: ", response['stopReason'])
print("Usage: ", json.dumps(response['usage'], indent=4, ensure_ascii=False))
