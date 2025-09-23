import os
import pandas as pd
from dotenv import load_dotenv
from typing import List
from langchain_core.documents import Document
from langchain_astradb import AstraDBVectorStore
from utils.model_loader import ModelLoader
from utils.config_loader import load_config

class DataIngestion:
    """Class to handle data transformation and ingestion into AstraDB vector store
    """
    def __init__(self):
        """Initialize the enviroment variables , embedding model, and set CSV file path.
        """
        print("Initializing DataIngestion pipeline...")
        self.model_loader = ModelLoader()
        self._load_env_variables()
        self.csv_path = self._get_csv_path()
        self.product_data = self._load_csv()
        self.config = load_config()

    def _load_env_variables(self):
        """Load environment variables from .env file
        """
        load_dotenv()

        required_vars = ["GOOGLE_API_KEY", "ASTRA_DB_API_ENDPOINT", "ASTRA_DB_APPLICATION_TOKEN", "ASTRA_DB_KEYSPACE"]
        
        missing_vars = [var for var in required_vars if os.getenv(var) is None] 
        if missing_vars:
            raise EnvironmentError(f"Missing required environment variables: {missing_vars}")
        
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.db_api_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
        self.db_application_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
        self.db_keyspace = os.getenv("ASTRA_DB_KEYSPACE")
        

    def _get_csv_path(self):
        """Get the path to the CSV file
        """
        current_dir = os.getcwd()
        csv_path = os.path.join(current_dir, "data", "product_reviews.csv")

        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found at: {csv_path}")
        
        return csv_path

    def _load_csv(self):
        """Load the CSV file into a pandas DataFrame
        """
        df = pd.read_csv(self.csv_path)
        
        expected_columns = {'product_id','product_title', 'rating', 'total_reviews','price', 'top_reviews'}

        if not expected_columns.issubset(set(df.columns)):
            raise ValueError(f"CSV must contain columns: {expected_columns}")
    
        return df
    
    def transform_data(self):
        """Transform the data into a list of documents
        """
        product_list = []

        for _, row in self.product_data.iterrows():
            product_entry = {
                "product_id": row["product_id"],
                "product_title": row["product_title"],
                "rating": row["rating"],
                "total_reviews": row["total_reviews"],
                "price": row["price"],
                "top_reviews": row["top_reviews"]
            }
            
            product_list.append(product_entry)

        documents = []
        for entry in product_list:
            metadata = {
                "product_id": entry["product_id"],
                "product_title": entry["product_title"],
                "rating": entry["rating"],
                "total_reviews": entry["total_reviews"],
                "price": entry["price"]
            }
            doc = Document(page_content=entry["top_reviews"], metadata=metadata)
            documents.append(doc)

        print(f"Transformed {len(documents)} documents.")
        return documents
    

    def store_data(self, documents: List[Document]):
        """Store the data into AstraDB vector store
        """
        collection_name = self.config["astra_db"]["collection_name"]
        vector_store = AstraDBVectorStore(
            embedding=self.model_loader.load_embeddings(),
            collection_name=collection_name,
            api_endpoint=self.db_api_endpoint,
            token=self.db_application_token,
            namespace=self.db_keyspace,
        )

        inserted_ids = vector_store.add_documents(documents)
        print(f"Successfully inserted {len(inserted_ids)} documents into AstraDB.")
        return vector_store, inserted_ids

    def run_pipeline(self):
        """Run the full data pipeline: transform data and store into vector DB.
        """
        documents = self.transform_data()
        vector_store, _ = self.store_data(documents)

        # Optionally do a quick search
        query = "Can you tellme the low budget iphone?"
        results = vector_store.similarity_search(query)

        print(f"\nSample search results for query: '{query}'")
        for res in results:
            print(f"Content: {res.page_content}\nMetadata: {res.metadata}\n")

        
# Run if this file is executed directly
if __name__ == "__main__":
    ingestion = DataIngestion()
    ingestion.run_pipeline()       
            