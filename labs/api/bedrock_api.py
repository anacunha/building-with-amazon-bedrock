import json
import boto3

session = boto3.Session()

bedrock = session.client(service_name='bedrock-runtime')

bedrock_model_id = 'amazon.titan-text-express-v1'

prompt = 'Qual a maior cidade da América Latina?'
print(prompt)

body = json.dumps({
    "inputText": prompt,
    "textGenerationConfig": {
        "temperature": 0,
        "topP": 0.5,
        "maxTokenCount": 1024,
        "stopSequences": []
    }
})

response = bedrock.invoke_model(
    body=body,
    modelId=bedrock_model_id,
    accept='application/json',
    contentType='application/json'
)

response_body = json.loads(response.get('body').read())
response_text = response_body["results"][0]["outputText"]

print(response_text)
