import json
import boto3

#
session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client

#
bedrock_model_id = "amazon.titan-text-express-v1" #set the foundation model

prompt = "What is the largest city in New Hampshire?" #the prompt to send to the model

body = json.dumps({
    "inputText": prompt,
    "textGenerationConfig": {
        "temperature": 0,  
        "topP": 0.5,
        "maxTokenCount": 1024,
        "stopSequences": []
    }
}) #build the request payload

#
response = bedrock.invoke_model(body=body, modelId=bedrock_model_id, accept='application/json', contentType='application/json') #send the payload to Amazon Bedrock

#
response_body = json.loads(response.get('body').read()) # read the response

response_text = response_body["results"][0]["outputText"] #extract the text from the JSON response

print(response_text)
