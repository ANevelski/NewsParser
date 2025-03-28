import os
import faiss
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from uuid import uuid4
from langchain_core.documents import Document

def save_to_vector_database(articles):  
     # Initialize embeddings
    subscription_key = os.getenv("AZURE_OPENAPI_KEY")
    embeddings = AzureOpenAIEmbeddings(model="text-embedding-3-large", azure_deployment="my-text-embedding-3-large", azure_endpoint="https://newsparser.openai.azure.com/", api_version="2024-12-01-preview",api_key=subscription_key)

    index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world"))) #len

    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={}
    )

    documents = []

    # Looping through a list of objects (JSON array)
    for item in articles:
            document = Document(
                page_content=item['sammary'],
                metadata={"topics": item['topics']},
            )
            documents.append(document)
            
    uuids = [str(uuid4()) for _ in range(len(documents))]
    vector_store.add_documents(documents=documents, ids=uuids)
    file_name = "News_faiss_index"
    vector_store.save_local(file_name)
    return file_name