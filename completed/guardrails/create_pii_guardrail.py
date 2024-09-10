import boto3, json, random, string, test_helper as glib


client = boto3.client(service_name='bedrock') #creates a Bedrock client

response = client.create_guardrail(
    name="PII-Masking-" + "".join(random.choices(string.ascii_lowercase, k=8)),
    description='string',
    sensitiveInformationPolicyConfig={
        "piiEntitiesConfig": [
            {"type": "NAME", "action": "ANONYMIZE"},
            {"type": "EMAIL", "action": "ANONYMIZE"},
        ],
    },
    blockedInputMessaging="Apologies, this model cannot be used to discuss inappropriate or off-topic content.",
    blockedOutputsMessaging="Apologies, the model's response to your request was blocked.",
)

guardrail_id = response['guardrailId']

response = client.create_guardrail_version(
    guardrailIdentifier=guardrail_id,
)

glib.set_guardrail_id('pii_masking_guardrail_id', guardrail_id)