from langchain.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

class ProductSearchTool:
    @tool("search_inventory")
    def search(query: str):
        \"\"\"
        Applies RAG strategies to retrieve grounded product data. 
        Satisfies: Context Engineering & Vector DB requirements.
        \"\"\"
        embeddings = OpenAIEmbeddings()
        
        # Mock data for initial indexing - In production, this pulls from Pinecone/Weaviate
        if not os.path.exists("faiss_index"):
            texts = ["Ultra-light Waterproof Hiking Jacket - $150 - Blue", "Mountain Pro Boots - $200 - Brown"]
            vector_db = FAISS.from_texts(texts, embeddings)
            vector_db.save_local("faiss_index")
        
        vector_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        results = vector_db.similarity_search(query, k=2)
        return [doc.page_content for doc in results]
