from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.embedding import EmbeddingPipeline
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    
    # docs = load_all_documents("data")# load documents only if building vector store for new documents
    store = FaissVectorStore("faiss_store")
    #store.build_from_documents(docs) # onlt run first time to build the store or if new documents added
    store.load()
    
    rag_search = RAGSearch()
    query = "What are the symptoms of Parkinsons Disease?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
  
   