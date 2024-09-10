import random, string, boto3, json, pprint, test_helper as glib

prompt = glib.get_prompt_from_command_line()
guardrail_id = glib.get_guardrail_id('content_blocking_guardrail_id')

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client

body = {
    "inputText": prompt,
    "textGenerationConfig": {
        "maxTokenCount": 512,
        "stopSequences": [],
        "temperature": 0,
        "topP": 0.9
    }
}

response = bedrock.invoke_model(
    body=json.dumps(body),
    modelId="amazon.titan-text-express-v1",
    contentType="application/json",
    accept="application/json",
    guardrailIdentifier=guardrail_id,
    guardrailVersion="DRAFT", #this is fine during development, but we should set this to a specific version number for testing and production.
)

response_body = json.loads(response.get('body').read()) # read the response

response_text = response_body['results'][0]['outputText']

print(response_text)