from langchain_community.llms import Bedrock

##################################################################

llm = Bedrock( #create a Bedrock llm client
    model_id="amazon.titan-text-express-v1" #set the foundation model
)

##################################################################

prompt = "What is the name of the largest city in Vermont? Just provide the name of the city:"
    
response_text = llm.invoke(prompt) #return a response to the prompt

print(response_text)
