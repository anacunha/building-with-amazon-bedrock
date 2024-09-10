import boto3, json, random, string, test_helper as glib

client = boto3.client(service_name='bedrock') #creates a Bedrock client

response = client.create_guardrail(
    name="Prompt-Attack-" + "".join(random.choices(string.ascii_lowercase, k=8)),
    description='string',
    contentPolicyConfig={
        'filtersConfig': [
            {"type": "PROMPT_ATTACK", "inputStrength": "HIGH", "outputStrength": "NONE"},
        ]
    },
    blockedInputMessaging="Apologies, your request was blocked.",
    blockedOutputsMessaging="Apologies, the model's response to your request was blocked.",
)

guardrail_id = response['guardrailId']

response = client.create_guardrail_version(
    guardrailIdentifier=guardrail_id,
)

glib.set_guardrail_id('prompt_attack_guardrail_id', guardrail_id)