# Libraries
import os
from langchain_astradb import AstraDBVectorStore
from typing import List
from langchain_core.documents import Document
from utils.config_loader import load_config
from utils.model_loader import ModelLoader
from dotenv import load_dotenv
import sys
from pathlib import Path


class Retreiver:
    def __init__(self):
        """_summary_
        """
        self.model_loader=ModelLoader()
        self.config=load_config()
        self._load_env_variables()
        self.vector_store=None
        self.retreiver=None

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
    
    def load_retreiver(self):
        """_summary_
        """
        if not self.vector_store:
            collection_name = self.config["astra_db"]["collection_name"]

            self.vector_store=AstraDBVectorStore(
                embedding=self.model_loader.load_embeddings(),
                collection_name=collection_name,
                api_endpoint=self.db_api_endpoint,
                token=self.db_application_token,
                namespace=self.db_keyspace,
            )
        if not self.retreiver:
            top_k = self.config["retriever"]["top_k"] if "retriever" in self.config else 3
            self.retreiver=self.vector_store.as_retriever(search_kwargs={"k": top_k})
            print("Retriver loaded Successufully")
        return self.retreiver
        
    def call_retreiver(self, user_query):
        """_summary_
        """
        retriver=self.load_retreiver()
        output=retriver.invoke(user_query)
        return output

if __name__ == "__main__":
    retreiver_obj = Retreiver()
    user_query = "Can you suggest good budget phone?"
    results = retreiver_obj.call_retreiver(user_query)

    for idx, doc in enumerate(results, 1):
        print(f"Result {idx}: {doc.page_content}\Metadat: {doc.metadata}\n")