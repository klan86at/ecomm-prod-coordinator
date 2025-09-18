import os
import pandas as pd
from dotenv import load_dotenv
from typing import List
from langchain_core.documents import Document
from langchain_astradb import AstraDBVectorStore
from prod_assistant.utils.model_loader import ModelLoader
from prod_assistant.utils.config_loader import load_config

class DataIngestion:
    """Class to handle data transformation and ingestion into AstraDB vector store
    """
    def __init__(self):
        pass
    def load_env_variables(self):
        """Load environment variables from .env file
        """
        pass
    def _get_csv_path(self):
        """Get the path to the CSV file
        """
        pass
    def _load_csv(self):
        """Load the CSV file into a pandas DataFrame
        """
        pass
    def transform_data(self):
        """Transform the data into a list of documents
        """
        pass
    def store_data(self):
        """Store the data into AstraDB vector store
        """
        pass
    def run_pipeline(self):
        """Run the pipeline
        """
        pass
            