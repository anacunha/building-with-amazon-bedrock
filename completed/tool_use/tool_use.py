import boto3, json, math

print("\n----Definindo uma tool and enviando uma mensagem que fara Claude solicitar o uso da tool----\n")

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

tool_list = [
    {
        "toolSpec": {
            "name": "coseno",
            "description": "Calcular o coseno de x.",
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {
                        "x": {
                            "type": "number",
                            "description": "O número apra passar para a função."
                        }
                    },
                    "required": ["x"]
                }
            }
        }
    }
]

message_list = []

initial_message = {
    "role": "user",
    "content": [
        { "text": "Qual é o coseno de 7?" } 
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
    toolConfig={
        "tools": tool_list
    },
    system=[{"text":"Você só deve fazer contas usando uma tool."}]
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4))
message_list.append(response_message)

print("\n----Chamando a função baseado no content block toolUse.----\n")

response_content_blocks = response_message['content']

for content_block in response_content_blocks:
    if 'toolUse' in content_block:
        tool_use_block = content_block['toolUse']
        tool_use_name = tool_use_block['name']
        
        print(f"Usando a tool {tool_use_name}")
        
        if tool_use_name == 'coseno':
            tool_result_value = math.cos(tool_use_block['input']['x'])
            print(tool_result_value)
            
    elif 'text' in content_block:
        print(content_block['text'])


print("\n----Passando o resultado da tool de volta para Claude----\n")

follow_up_content_blocks = []

for content_block in response_content_blocks:
    if 'toolUse' in content_block:
        tool_use_block = content_block['toolUse']
        tool_use_name = tool_use_block['name']
        
        
        if tool_use_name == 'coseno':
            tool_result_value = math.cos(tool_use_block['input']['x'])
            
            follow_up_content_blocks.append({
                "toolResult": {
                    "toolUseId": tool_use_block['toolUseId'],
                    "content": [
                        {
                            "json": {
                                "result": tool_result_value
                            }
                        }
                    ]
                }
            })

if len(follow_up_content_blocks) > 0:
    
    follow_up_message = {
        "role": "user",
        "content": follow_up_content_blocks,
    }
    
    message_list.append(follow_up_message)

    response = bedrock.converse(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        messages=message_list,
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0
        },
        toolConfig={
            "tools": tool_list
        },
        system=[{"text":"Você só deve fazer contas usando uma tool."}]
    )
    
    response_message = response['output']['message']
    
    message_list.append(response_message)
    print(json.dumps(message_list, indent=4))

