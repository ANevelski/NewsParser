import os
import faiss
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from uuid import uuid4
from langchain_core.documents import Document

# Function for creating vector database file
def save_to_vector_database_file(articles): 
    try: 
        # Initialize embeddings
        subscription_key = os.getenv("AZURE_OPENAPI_KEY")
        embeddings = AzureOpenAIEmbeddings(model="text-embedding-3-large", azure_deployment="my-text-embedding-3-large", azure_endpoint="https://newsparser.openai.azure.com/", api_version="2024-12-01-preview",api_key=subscription_key)

        # Prepare an index for storing and performing vector similarity searches
        index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world"))) 

        # Create vector store
        vector_store = FAISS(
            embedding_function=embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={}
        )

        articles_data = []
        # Looping through a list of objects (JSON array)
        for article in articles:
            document = Document(
                page_content=article['summary'],
                metadata={"topics": article['topics']},
            )
            articles_data.append(document)

        # Save data to file
        uuids = [str(uuid4()) for _ in range(len(articles_data))] # This statement creates a list of string values ​​representing unique identifiers (UUIDs) for the number of items in articles_data.
        vector_store.add_documents(documents=articles_data, ids=uuids)
        file_name = "News_faiss_index"
        vector_store.save_local(file_name)

        return file_name
    except Exception:
        print(f"Error during saving to vector database file. No data to save.")
        return None