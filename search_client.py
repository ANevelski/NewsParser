import os
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def similarity_search(file_name):
    # Initialize embeddings
    subscription_key = os.getenv("AZURE_OPENAPI_KEY")
    embeddings = AzureOpenAIEmbeddings(model="text-embedding-3-large", azure_deployment="my-text-embedding-3-large", azure_endpoint="https://newsparser.openai.azure.com/", api_version="2024-12-01-preview",api_key=subscription_key)
        
    vector_store = FAISS.load_local(file_name, embeddings, allow_dangerous_deserialization = True)

    # Search for the text    
    results = vector_store.similarity_search(
         "Do you have some BBC news?",
         k=2
    )

    # Printing the results
    for result in results:
        print(result.page_content)