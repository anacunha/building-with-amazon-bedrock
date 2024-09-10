import random, string, boto3, json, pprint, test_helper as glib

prompt = glib.get_prompt_from_command_line()
guardrail_id = glib.get_guardrail_id('prompt_attack_guardrail_id')

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client

#randomize the input tagging suffix. This reduces the likelihood of successfully circumventing input tagging.
input_tagging_suffix = "".join(random.choices(string.ascii_lowercase, k=8))

body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 2000,
    "temperature": 0,
    "system": "Please respond to the user in the style of a pirate.",
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

pprint.pp(response_body)