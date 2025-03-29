import os
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Function for perform search from vector DataBase file
def similarity_search(file_name):
    try:
          # Initialize embeddings
          subscription_key = os.getenv("AZURE_OPENAPI_KEY")
          embeddings = AzureOpenAIEmbeddings(model="text-embedding-3-large", azure_deployment="my-text-embedding-3-large", azure_endpoint="https://newsparser.openai.azure.com/", api_version="2024-12-01-preview",api_key=subscription_key)
               
          # Load vector DataBase file
          vector_store = FAISS.load_local(file_name, embeddings, allow_dangerous_deserialization = True)

          # Search for the text    
          results = vector_store.similarity_search(
               "Do you have some BBC news?",
               k=5
          )
          return results
    except Exception:
        print(f"Error during searching from vector database file. File was not found.")
        return None