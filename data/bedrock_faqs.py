#From https://aws.amazon.com/bedrock/faqs/ July 18, 2024
import json

faqs = [

{
"question": "What is Amazon Bedrock?",
"answer": """Amazon Bedrock is a fully managed service that offers a choice of industry leading foundation models (FMs) along with a broad set of capabilities that you need to build generative AI applications, simplifying development with security, privacy, and responsible AI. With the comprehensive capabilities of Amazon Bedrock, you can experiment with a variety of top FMs, customize them privately with your data using techniques such as fine-tuning and retrieval-augmented generation (RAG), and create managed agents that execute complex business tasks—from booking travel and processing insurance claims to creating ad campaigns and managing inventory—all without writing any code. Since Amazon Bedrock is serverless, you don't have to manage any infrastructure, and you can securely integrate and deploy generative AI capabilities into your applications using the AWS services you are already familiar with.
"""
},

{
"question": "Which FMs are available on Amazon Bedrock? ",
"answer": """

Amazon Bedrock customers can choose from some of the most cutting-edge FMs available today. This includes language and embeddings models from:

    AI21 Labs: Jurassic – 2 Ultra, Jurassic – 2 Mid
    Anthropic: Claude 3 Opus, Claude 3 Sonnet, Claude 3 Haiku
    Cohere: Command R, Command R+, Embed
    Meta: Llama 3 8B, Llama 3 70B
    Mistral AI: Mistral 8X7B Instruct, Mistral 7B Instruct, Mistral Large, Mistral Small
    Stability AI: Stable Diffusion XL 1.0
    Amazon Titan: Amazon Titan Text Premier, Amazon Titan Text Express, Amazon Titan Text Lite, Amazon Titan Text Embeddings, Amazon Titan Text Embeddings V2, Amazon Titan Multimodal Embeddings, Amazon Titan Image Generator


"""
},


{
"question": "Why should I use Amazon Bedrock?",
"answer": """

There are five reasons to use Amazon Bedrock for building generative AI applications.

    Choice of leading FMs: Amazon Bedrock offers an easy-to-use developer experience to work with a broad range of high-performing FMs from Amazon and leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, and Stability AI. You can quickly experiment with a variety of FMs in the playground, and use a single API for inference regardless of the models you choose, giving you the flexibility to use FMs from different providers and keep up to date with the latest model versions with minimal code changes.
    Easy model customization with your data: Privately customize FMs with your own data through a visual interface without writing any code. Simply select the training and validation data sets stored in Amazon Simple Storage Service (Amazon S3) and, if required, adjust the hyperparameters to achieve the best possible model performance.
    Fully managed agents that can invoke APIs dynamically to execute tasks: Build agents that execute complex business tasks—from booking travel and processing insurance claims to creating ad campaigns, preparing tax filings, and managing your inventory—by dynamically calling your company systems and APIs. Fully managed agents for Amazon Bedrock extend the reasoning capabilities of FMs to break down tasks, create an orchestration plan, and execute it.
    Native support for RAG to extend the power of FMs with proprietary data: With Knowledge Bases for Amazon Bedrock, you can securely connect FMs to your data sources for retrieval augmentation—from within the managed service—extending the FM’s already powerful capabilities and making it more knowledgeable about your specific domain and organization.
    Data security and compliance certifications: Amazon Bedrock offers several capabilities to support security and privacy requirements. Amazon Bedrock is in scope for common compliance standards such as Service and Organization Control (SOC), International Organization for Standardization (ISO), is Health Insurance Portability and Accountability Act (HIPAA) eligible, and customers can use Amazon Bedrock in compliance with the General Data Protection Regulation (GDPR). Amazon Bedrock is CSA Security Trust Assurance and Risk (STAR) Level 2 certified, which validates the use of best practices and the security posture of AWS cloud offerings. With Amazon Bedrock, your content is not used to improve the base models and is not shared with any model providers. Your data in Amazon Bedrock is always encrypted in transit and at rest, and you can optionally encrypt the data using your own keys. You can use AWS PrivateLink with Amazon Bedrock to establish private connectivity between your FMs and your Amazon Virtual Private Cloud (Amazon VPC) without exposing your traffic to the Internet.


"""
},

{
"question": "How can I get started with Amazon Bedrock?",
"answer": """With the serverless experience of Amazon Bedrock, you can quickly get started. Navigate to Amazon Bedrock in the AWS Management Console and try out the FMs in the playground. You can also create an agent and test it in the console. Once you’ve identified your use case, you can easily integrate the FMs into your applications using AWS tools without having to manage any infrastructure.
"""
},

{
"question": "What are the most common use cases for Amazon Bedrock?",
"answer": """You can quickly get started with use cases:

    Create new pieces of original content, such as short stories, essays, social media posts, and web page copy.
    Search, find, and synthesize information to answer questions from a large corpus of data.
    Create realistic and artistic images of various subjects, environments, and scenes from language prompts.
    Help customers find what they’re looking for with more relevant and contextual product recommendations than word matching.
    Get a summary of textual content such as articles, blog posts, books, and documents to get the gist without having to read the full content.
    Suggest products that match shopper preferences and past purchases

"""
},

{
"question": "What is Amazon Bedrock Playground?",
"answer": """Amazon Bedrock offers a playground that allows you to experiment with various FMs using a conversational chat interface. You can provide a prompt and use a web interface inside the console to supply a prompt and use the pretrained models to generate text or images, or alternatively use a fine-tuned model that has been adapted for your use case.
"""
},

{
"question": "In which AWS Regions is Amazon Bedrock available?",
"answer": """For a list of AWS Regions where Amazon Bedrock is available, see Amazon Bedrock endpoints and quotas in the Amazon Bedrock Reference Guide.
"""
},

{
"question": "How do I customize a model on Amazon Bedrock?",
"answer": """You can easily fine-tune FMs on Amazon Bedrock using tagged data or by using continued pre-train feature to customize the model using non-tagged data. To get started, provide the training and validation dataset, configure hyperparameters (epochs, batch size, learning rate, warmup steps) and submit the job. Within a couple of hours, your fine-tuned model can be accessed with the same API (InvokeModel).
"""
},

{
"question": "Can I train a model and deploy it on Amazon Bedrock?",
"answer": """Yes, you can train select publicly available models and import them into the Amazon Bedrock using the Custom Model Import feature. Currently, this feature only supports Llama 2/3, Mistral, and Flan architectures. For additional information, please refer the documentation.
"""
},

{
"question": "What are Agents for Amazon Bedrock?",
"answer": """Agents for Amazon Bedrock are fully managed capabilities that make it easier for developers to create generative AI–based applications that can complete complex tasks for a wide range of use cases and deliver up-to-date answers based on proprietary knowledge sources. In just a few short steps, Agents for Amazon Bedrock automatically break down tasks and create an orchestration plan–without any manual coding. The agent securely connects to company data through an API, automatically converting data into a machine-readable format, and augmenting the request with relevant information to generate the most accurate response. Agents can then automatically call APIs to fulfill a user’s request. For example, a manufacturing company might want to develop a generative AI application that automates tracking inventory levels, sales data, supply chain information and that can recommend optimal reorder points and quantities to maximize efficiency. As fully managed capabilities, Agents for Amazon Bedrock remove the undifferentiated lifting of managing system integration and infrastructure provisioning, allowing developers to use generative AI to its full extent throughout their organization.
"""
},

{
"question": "How can I connect FMs to my company data sources?",
"answer": """You can securely connect FMs to your company data sources using Agents for Amazon Bedrock. With a knowledge base, you can use agents to give FMs in Amazon Bedrock access to additional data that helps the model generate more relevant, context-specific, and accurate responses without continually retraining the FM. Based on user input, agents identify the appropriate knowledge base, retrieve the relevant information, and add the information to the input prompt, giving the model more context information to generate a completion.
"""
},

{
"question": "What are some use cases for Agents for Amazon Bedrock?",
"answer": """Agents for Amazon Bedrock can help you increase productivity, improve your customer service experience, and automate workflows (such as processing insurance claims).
"""
},


{
"question": "How do Agents for Amazon Bedrock help improve developer productivity?",
"answer": """

With agents, developers have seamless support for monitoring, encryption, user permissions, versioning, and API invocation management without writing custom code. Agents for Amazon Bedrock automate the prompt engineering and orchestration of user-requested tasks. Developers can use the agent-created prompt template as a baseline to further refine it for an enhanced user experience. They can update the user input, orchestration plan, and the FM response. With access to the prompt template developers have better control over the Agent orchestration.

With fully managed agents, you don’t have to worry about provisioning or managing infrastructure and can take applications to production faster.

"""
},

{
"question": "Is the content processed by Amazon Bedrock moved outside the AWS Region where I am using Amazon Bedrock?",
"answer": """Any customer content processed by Amazon Bedrock is encrypted and stored at rest in the AWS Region where you are using Amazon Bedrock.
"""
},

{
"question": "Are user inputs and model outputs made available to third-party model providers?",
"answer": """No. Users' inputs and model outputs are not shared with any model providers.
"""
},

{
"question": "What security and compliance standards does Amazon Bedrock support?",
"answer": """Amazon Bedrock offers several capabilities to support security and privacy requirements. Amazon Bedrock is in scope for common compliance standards such as Fedramp Moderate, Service and Organization Control (SOC), International Organization for Standardization (ISO), Health Insurance Portability and Accountability Act (HIPAA) eligibility, and customers can use Bedrock in compliance with the General Data Protection Regulation (GDPR). Amazon Bedrock is included in the scope of the SOC 1, 2, 3 reports, allowing customers to gain insights into our security controls. We demonstrate compliance through extensive third-party audits of our AWS controls. Amazon Bedrock is one of the AWS services under ISO Compliance for the ISO 9001, ISO 27001, ISO 27017, ISO 27018, ISO 27701, ISO 22301, and ISO 20000 standards. Amazon Bedrock is CSA Security Trust Assurance and Risk (STAR) Level 2 certified, which validates the use of best practices and the security posture of AWS cloud offerings. With Amazon Bedrock, your content is not used to improve the base models and is not shared with any model providers. You can use AWS PrivateLink to establish private connectivity from Amazon VPC to Amazon Bedrock, without having to expose your data to internet traffic.
"""
},

{
"question": "Will AWS and third-party model providers use customer inputs to or outputs from Amazon Bedrock to train Amazon Titan or any third-party models?",
"answer": """No, AWS and the third-party model providers will not use any inputs to or outputs from Amazon Bedrock to train Amazon Titan or any third-party models.
"""
},

{
"question": "What SDKs are supported for Amazon Bedrock?",
"answer": """Amazon Bedrock supports SDKs for runtime services. iOS and Android SDKs, as well as Java, JS, Python, CLI, .Net, Ruby, PHP, Go, and C++.
"""
},

{
"question": "What SDKs support streaming functionality?",
"answer": """Streaming is supported on all the SDKs.
"""
},

{
"question": "How much does Amazon Bedrock cost?",
"answer": """Please see the Amazon Bedrock pricing page for current pricing information.
"""
},

{
"question": "What support is provided for Amazon Bedrock?",
"answer": """Depending on your AWS Support contract, Amazon Bedrock is supported under Developer Support, Business Support and Enterprise Support plans.
"""
},

{
"question": "How can I track the input and output tokens?",
"answer": """You can use CloudWatch metrics to track the input and output tokens.
"""
},


{
"question": "How can I securely use my data to customize FMs available through Amazon Bedrock?",
"answer": """With Amazon Bedrock, you can privately customize FMs, retaining control over how your data is used and encrypted. Amazon Bedrock makes a separate copy of the base FM and trains this private copy of the model. Your data including prompts, information used to supplement a prompt, and FM responses. Customized FMs remain in the Region where the API call is processed.
"""
},

{
"question": "How does Amazon Bedrock ensure my data used in fine-tuning remains private and confidential?",
"answer": """When you’re fine-tuning a model, your data is never exposed to the public internet, never leaves the AWS network, is securely transferred through your VPC, and is encrypted in transit and at rest. Amazon Bedrock also enforces the same AWS access controls that you have with any of our other services.
"""
},

{
"question": "Does Amazon Bedrock support continued pretraining?",
"answer": """We launched continued pretraining for Amazon Titan Text Express and Amazon Titan models on Amazon Bedrock. Continued pretraining allows you to continue the pretraining on an Amazon Titan base model using large amounts of unlabeled data. This type of training will adapt the model from a general domain corpus to a more specific domain corpus such as medical, law, finance, and so on, while still preserving most of the capabilities of the Amazon Titan base model. 
"""
},

{
"question": "Why should I use continued pretraining in Amazon Bedrock?",
"answer": """Enterprises may want to build models for tasks in a specific domain. The base models may not be trained on the technical jargon used in that specific domain. Thus, directly fine-tuning the base model requires large amounts of labeled training records and a long training duration to get accurate results. To ease this burden, the customer can instead provide large amounts of unlabeled data for a continued pretraining job. This job will adapt the Amazon Titan base model to the new domain. Then the customer may fine-tune the newly pretrained custom model to downstream tasks, using significantly fewer labeled training records and with a shorter training duration. 
"""
},

{
"question": "How does the continued pretraining feature relate to other AWS services?",
"answer": """Amazon Bedrock continued pretraining and fine-tuning have very similar requirements. For this reason, we are choosing to create unified APIs that support both continued pretraining and fine-tuning. Unification of the APIs reduces the learning curve and will help customers use standard features such as Amazon EventBridge to track long running jobs, Amazon S3 integration for fetching training data, resource tags, and model encryption. 
"""
},

{
"question": "How do I use continued pre-training?",
"answer": """Continued pretraining helps you adapt the Amazon Titan models to your domain specific data while still preserving the base functionality of the Amazon Titan models. To create a continued pretraining job, navigate to the Amazon Bedrock console and click on "Custom Models." You will navigate to the custom model page that has two tabs: Models and Training jobs. Both tabs provide a “Customize Model” drop-down menu on the right. Select “Continued Pretraining” from the drop-down menu to navigate to “Create Continued Pretraining Job." You will provide the source model, name, model encryption, input data, hyper-parameters and output data. Additionally, you can provide tags, along with details about AWS Identity and Access Management (IAM) roles and resource policies for the job.
"""
},

{
"question": "What are Amazon Titan models? ",
"answer": """Exclusive to Amazon Bedrock, the Amazon Titan family of models incorporates 25 years of Amazon experience innovating with AI and machine learning across the business. Amazon Titan FMs provide customers with a breadth of high-performing image, multimodal, and text model choices through a fully managed API. Amazon Titan models are created by AWS and pretrained on large datasets, making them powerful, general-purpose models built to support a variety of use cases, while also supporting the responsible use of AI. Use them as is or privately customize them with your own data.
"""
},

{
"question": "Where can I learn more about the data processed to develop and train Amazon Titan FMs?",
"answer": """To learn more about data processed to develop and train Amazon Titan FMs, visit Amazon Titan Model Training and Privacy page.
"""
},

{
"question": "What types of data formats are accepted by Knowledge Bases for Amazon Bedrock?",
"answer": """Supported data formats include .pdf, .txt, .md, .html, .doc and .docx, .csv, .xls, and .xlsx files. Files must be uploaded to Amazon S3. Point to the location of your data in Amazon S3, and Knowledge Bases for Amazon Bedrock takes care of the entire ingestion workflow into your vector database.
"""
},

{
"question": "How does Knowledge Bases for Amazon Bedrock chunk the documents before converting those chunks to embeddings?",
"answer": """Knowledge Bases for Amazon Bedrock provides three options to chunk text before converting it to embeddings. 

1.  Default option: Knowledge Bases for Amazon Bedrock automatically splits your document into chunks each containing 200 tokens, ensuring that a sentence is not broken in the middle. If a document contains less than 200 tokens, then it is not split any further. An overlap of 20% of tokens is maintained between two consecutive chunks.

2.  Fixed size chunking: In this option, you can specify the maximum number of tokens per chunk and the overlap percentage between chunks for Knowledge Bases for Amazon Bedrock, so your document will be automatically split into chunks, ensuring that a sentence is not broken in the middle. 

3.  Create one embedding per document option: Amazon Bedrock creates one embedding per document. This option is suitable if you have preprocessed your documents by splitting them into separate files and do not want Amazon Bedrock to further chunk your documents.
"""
},


{
"question": "Which embeddings model is used to convert documents into embeddings (vectors)?",
"answer": """At present, Knowledge Bases for Amazon Bedrock uses the latest version of the Amazon Titan Text Embeddings model available in Amazon Bedrock. Titan Text Embeddings V2 model supports 8K tokens and 100+ languages and creates an embeddings of flexible 256, 512, and 1,024 dimension size. 
"""
},

{
"question": "Which vector databases are supported by Knowledge Bases for Amazon Bedrock?",
"answer": """Knowledge Bases for Amazon Bedrock takes care of the entire ingestion workflow of converting your documents into embeddings (vector) and storing the embeddings in a specialized vector database. Knowledge Bases for Amazon Bedrock supports popular databases for vector storage, including vector engine for Amazon OpenSearch Serverless, Pinecone, Redis Enterprise Cloud, Amazon Aurora (coming soon), and MongoDB (coming soon). If you do not have an existing vector database, Amazon Bedrock creates an OpenSearch Serverless vector store for you.
"""
},

{
"question": "Is it possible to do a periodic or event-driven sync from Amazon S3 to Knowledge Bases for Amazon Bedrock?",
"answer": """Depending on your use case, you can use Amazon EventBridge to create a periodic or event-driven sync between Amazon S3 and Knowledge Bases for Amazon Bedrock.
"""
},

{
"question": "What is Model Evaluation on Amazon Bedrock?",
"answer": """Model Evaluation on Amazon Bedrock allows you to evaluate, compare, and select the best FM for your use case in just a few short steps. Amazon Bedrock offers a choice of automatic evaluation and human evaluation. You can use automatic evaluation with predefined metrics such as accuracy, robustness, and toxicity. You can use human evaluation workflows for subjective or custom metrics such as friendliness, style, and alignment to brand voice. For human evaluation, you can use your in-house employees or an AWS-managed team as reviewers. Model Evaluation on Amazon Bedrock provides built-in curated datasets or you can bring your own datasets.
"""
},

{
"question": "Against what metrics can I evaluate FMs?",
"answer": """You can evaluate variety of predefined metrics such as accuracy, robustness, and toxicity using automatic evaluations. You can also use human evaluation workflows for subjective or custom metrics, such as friendliness, relevance, style, and alignment to brand voice.
"""
},

{
"question": "What is the difference between human-based and automatic evaluations?",
"answer": """Automatic evaluations allow you to quickly narrow down the list of available FMs against standard criteria (such as accuracy, toxicity and robustness). Human-based evaluations are often used to evaluate more nuanced or subjective criteria that require human judgment and where automatic evaluations might not exist (such as brand voice, creative intent, friendliness).
"""
},

{
"question": "How does automatic evaluation work?",
"answer": """You can quickly evaluate Amazon Bedrock models for metrics such as accuracy, robustness, and toxicity by using curated built-in data sets or by bringing your own prompt datasets. After your prompt datasets are sent to Amazon Bedrock models for inference, the model responses are scored with evaluation algorithms for each dimension. The backend engine aggregates individual prompt response scores into summary scores and presents them through easy-to-understand visual reports.
"""
},

{
"question": "How does human evaluation work?",
"answer": """Amazon Bedrock allows you to set up human review workflows in a few short steps and bring your in-house employees, or use an expert team managed by AWS, to evaluate models. Through Amazon Bedrock’s intuitive interface, humans can review and give feedback on model responses by clicking thumbs up or down, rating on a scale of 1-5, choosing the best of multiple responses, or ranking prompts. For example, a team member can be shown how two models respond to the same prompt, and then be asked to select the model that shows more accurate, relevant, or stylistic outputs. You can specify the evaluation criteria that matter to you by customizing the instructions and buttons to appear on the evaluation UI for your team. You can also provide detailed instructions with examples and the overall goal of model evaluation, so users can align their work accordingly. This method is useful to evaluate subjective criteria that require human judgement or more nuanced subject matter expertise and that cannot be easily judged by automatic evaluations.
"""
},

{
"question": "What are Guardrails for Amazon Bedrock?",
"answer": """Guardrails for Amazon Bedrock help you implement safeguards for your generative AI applications based on your use cases and responsible AI policies. Guardrails helps control the interaction between users and FMs by filtering undesirable and harmful content and will soon redact personally identifiable information (PII), enhancing content safety and privacy in generative AI applications. You can create multiple guardrails with different configurations tailored to specific use cases. Additionally, with the guardrails you can continually monitor and analyze user inputs and FM responses that might violate customer-defined policies.
"""
},

{
"question": "What are the safeguards available in Guardrails for Amazon Bedrock?",
"answer": """

Guardrails allows you to define a set of policies to help safeguard your generative AI applications. You can configure the following policies in a guardrail.

    Denied topics: define a set of topics that are undesirable in the context of your application. For example, an online banking assistant can be designed to refrain from providing investment advice.
    Content filters: configure thresholds to filter harmful content across hate, insults, sexual, and violence categories.
    Word filters (coming soon): define a set of words to block in user inputs and FM–generated responses.
    PII redaction (coming soon): select a set of PII that can be redacted in FM–generated responses. Based on the use case, you can also block a user input if it contains PII.


"""
},


{
"question": "Can I use guardrails with all available FMs and tools on Amazon Bedrock?",
"answer": """Guardrails can be used with all large language models (LLMs) available on Amazon Bedrock. It can also be used with fine-tuned FMs as well as Agents for Amazon Bedrock.
"""
},

{
"question": "Does AWS offer an intellectual property indemnity covering copyright claims for its generative AI services?",
"answer": """

AWS offers an uncapped intellectual property (IP) indemnity for copyright claims arising from generative output of the following generally available Amazon generative AI services: Amazon Titan models, Amazon CodeWhisperer Professional, and other services listed in Section 50.10 of the Service Terms (the “Indemnified Generative AI Services”). This means that customers are protected from third-party claims alleging copyright infringement by the output generated by the Indemnified Generative AI Services in response to inputs or other data provided by the customer. Customers must also use the services responsibly, such as not inputting infringing data or disabling a service’s filtering features.

In addition, our standard IP indemnity for use of the services protects customers from third-party claims alleging IP infringement (including copyright claims) by the services and the data used to train them.

"""
},

{
"question": "Do you have a list of off-the-shelf (built-in) guardrails, and what can be customized?",
"answer": """

There are four guardrail policies each with different off-the-shelf protections

    Content filters – This has 6 off the shelf categories (hate, insults, sexual, violence, misconduct (incl. criminal activity) and prompt attack (jailbreak and prompt injection. Each category can have further customized thresholds in terms of aggressiveness of filtering - low/medium/high.
    Denied topic – these are customized topics that customer can define using simple natural language description
    Sensitive information filter – these come with 30+ off the shelf PIIs. It can be further customized by adding customer’s proprietary information that are sensitive.
    Word filters – It comes with off the shelf profanity filtering and can be further customized with custom words.


"""
},

{
"question": "Do default guardrails automatically detect social security numbers or phone numbers?",
"answer": """Foundations model have native safeguards and they are the default protections associated with each model. These native safeguards are NOT part of guardrails for Amazon Bedrock. Guardrails is an added layer of customized safeguards that can be optionally applied by the customer based on their application requirements and responsible AI policies.


As part of Guardrails, SSN and phone number detection are part of the 30+ off the shelf PIIs. 
"""
},

{
"question": "Is there a separate cost for customers to build custom guardrails? And it is applied to both the input and output?",
"answer": """There is a separate cost for using guardrails. It can be applied for both input and output. 
"""
},

{
"question": "Are customers able to run automated tests on the effectiveness of the guardrails they set? Is there a “test case builder” (the journalist’s terminology) for ongoing monitoring?",
"answer": """Yes, customers can run automated test using Guardrail APIs. “Test case builder” maybe something you want to use prior to deploying guardrail in production. There is no native test case builder yet. For ongoing monitoring of production traffic, guardrails provide detailed logs of all violation for each input and output, so that customers can granularly monitor each and every input coming and going out of their gen AI application. These logs can be stored in CloudWatch or S3 and can be used to create custom dashboards based on customers’ requirements.
"""
},


]


with open('bedrock_faqs.json', 'w') as json_file:
    json.dump(faqs, json_file)


print("Saved JSON to disk!")