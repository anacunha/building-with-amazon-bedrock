import boto3, json, random, string, os, sys, configparser

def get_text_response(prompt):
    
    guardrail_variation = sys.argv[1] #we expect a legitimate ini key reference to be passed to the streamlit app.
    
    try:
        config = configparser.ConfigParser()
        config.read('bwab_guardrails.ini')
        guardrail_id = config['guardrails'][guardrail_variation]
    except:
        raise KeyError("Please run the appropriate create guardrail script indicated in the lab instructions.")
    
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    
    #randomize the input tagging suffix. This reduces the likelihood of successfully circumventing input tagging.
    input_tagging_suffix = "".join(random.choices(string.ascii_lowercase, k=8))
    
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 2000,
        "temperature": 0,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"<amazon-bedrock-guardrails-guardContent_{input_tagging_suffix}>{prompt}</amazon-bedrock-guardrails-guardContent_{input_tagging_suffix}>"},
                ],
            }
        ],
        "amazon-bedrock-guardrailConfig": {
            "tagSuffix": input_tagging_suffix
        }
    }
    
    response = bedrock.invoke_model(
        body=json.dumps(body),
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        contentType="application/json",
        accept="application/json",
        guardrailIdentifier=guardrail_id,
        guardrailVersion="DRAFT", #this is fine during development, but we should set this to a specific version number for testing and production.
        trace="ENABLED" #Set trace to "ENABLED" to see the details of guardrail actions, otherwise set to "DISABLED"
    )
    
    response_body = json.loads(response.get('body').read()) # read the response
    
    output = response_body['content'][0]['text']
    
    trace = response_body.get('amazon-bedrock-trace', {})
    
    guardrail_action = response_body.get('amazon-bedrock-guardrailAction', '')
    
    return output, guardrail_action, trace
