# ecomm-prod-coordinator

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Overview

The `ecomm-prod-coordinator` project introduces an intelligent AI-powered assistant specifically engineered for the demands of modern e-commerce product management. Its primary purpose is to streamline complex product-related workflows by harnessing advanced generative AI techniques, including Retrieval-Augmented Generation (RAG) and sophisticated agentic systems. This solution aims to transform how businesses gather, process, and act upon vast amounts of product data, from internal reviews to external web information.

At its core, `ecomm-prod-coordinator` leverages multi-step agentic workflows that can autonomously perform tasks like scraping web data, conducting targeted product searches, and synthesizing comprehensive insights from diverse sources, such as product reviews. It features a robust data pipeline for ingestion and transformation, ensuring that the AI has access to accurate and up-to-date information. The system also includes dedicated evaluation mechanisms to maintain the quality and reliability of its AI-generated outputs, making it a dependable tool for critical business functions.

This project is designed for e-commerce product managers, marketing professionals, content creators, and business analysts seeking to enhance their product strategy and operational efficiency. By automating the synthesis of product information and enabling intelligent content generation, `ecomm-prod-coordinator` empowers teams to make data-driven decisions faster, develop compelling product narratives, and respond more agilely to market trends. It offers a scalable, production-ready architecture, evident in its Kubernetes deployments, ensuring reliability for enterprise-level use.

## ✨ Features

Here's the README content for 'ecomm-prod-coordinator':

***

# ecomm-prod-coordinator

## Project Summary

The `ecomm-prod-coordinator` is an AI-powered system designed to assist with e-commerce product management. It leverages advanced Retrieval-Augmented Generation (RAG) and agentic workflows to intelligently process product information, handle queries, and coordinate tasks. The system includes modules for automated product data scraping and ingestion, a dedicated product search server, and robust evaluation mechanisms for its generative AI components. It's built for cloud-native deployment using Kubernetes and provides a web-based interface for interaction.

## Key Features

*   ✨ **AI-Powered Product Coordination**: Leverages advanced AI to streamline e-commerce product management and generate intelligent insights.
*   🧠 **Agentic RAG Workflows**: Implements sophisticated Retrieval-Augmented Generation with agentic capabilities for complex query handling and task execution.
*   🔍 **Integrated Product Search Engine**: Provides a dedicated, server-side component for efficient and accurate product information retrieval.
*   📊 **Automated Data Scraping & Ingestion**: Efficiently collects, processes, and ingests product reviews and other relevant data from various sources.
*   ☁️ **Cloud-Native Kubernetes Deployment**: Designed for scalable and resilient deployment on Kubernetes (EKS) with containerized services.
*   ✅ **Comprehensive RAG Evaluation**: Incorporates the RAGAS framework for rigorous assessment and continuous improvement of generative AI models.
*   🌐 **Intuitive Web-based Interface**: Offers a user-friendly web UI for interacting with the product coordinator and managing data scraping operations.

***

*   ✨ AI-powered e-commerce product coordination and assistance
*   🧠 Advanced Agentic Retrieval-Augmented Generation (RAG) workflows
*   🔍 Dedicated product search server for efficient data retrieval
*   📊 Automated product data scraping and intelligent ingestion
*   ☁️ Cloud-native deployment architecture using Kubernetes (EKS)
*   ✅ Integrated RAGAS framework for robust LLM/RAG evaluation
*   🌐 Intuitive web-based UI for seamless user interaction

## 📦 Installation

```bash
pip install ecomm-prod-coordinator
```

Or install from source:
```bash
git clone https://github.com/klan86at/ecomm-prod-coordinator.git
cd ecomm-prod-coordinator
pip install -e .
```

## 🚀 Quick Start

To get 'ecomm-prod-coordinator' up and running quickly, follow these steps:

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-org/ecomm-prod-coordinator.git
    cd ecomm-prod-coordinator
    ```
2.  **Set up Python Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  **Configure Environment Variables**
    Copy `.env.copy` to `.env` and fill in required API keys (e.g., LLM, search services).
    ```bash
    cp .env.copy .env
    # Edit .env
    ```
4.  **Run the Application**
    The project uses `uvicorn` to serve the web application.
    ```bash
    uvicorn prod_assistant.router.main:app --host 0.0.0.0 --port 8000
    ```
    Access the E-commerce Product Coordinator in your browser at `http://localhost:8000` to interact with the AI assistant.

## 📁 Project Structure

```
ecomm-prod-coordinator/
├── data
│   └── product_reviews.csv
├── infra
│   └── eks-with-ecr.yaml
├── k8
│   ├── deployment.yaml
│   └── service.yaml
├── logs
│   
│   
│   
│   
│   
│   
│   
├── notebook
│   └── test.ipynb
├── prod_assistant
│   ├── config
│   │   ├── __init__.py
│   │   └── config.yaml
│   ├── etl
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   └── data_scrapper.py
│   ├── evaluation
│   │   ├── __init__.py
│   │   └── ragas_eval.py
│   ├── exception
│   │   ├── __init__.py
│   │   └── custom_exception.py
│   ├── logger
│   │   ├── __init__.py
│   │   └── custom_logger.py
│   ├── mcp_servers
│   │   ├── client.py
│   │   └── product_search_server.py
│   ├── prompt_library
│   │   ├── __init__.py
│   │   └── prompts.py
│   ├── retreiver
│   │   ├── __init__.py
│   │   └── retreival.py
│   ├── router
│   │   └── main.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── config_loader.py
│   │   └── model_loader.py
│   ├── workflow
│   │   ├── __init__.py
│   │   ├── agentic_rag_workflow.py
│   │   ├── agentic_workflow_with_mcp.py
│   │   ├── agentic_workflow_with_mcp_websearch.py
│   │   └── normal_generation_workflow.py
│   └── __init__.py
├── static
│   ├── f6634145-b9d9-4ea1-b5e5-cb705192c6fd.png
│   └── style.css
├── templates
│   └── chat.html
├── .dockerignore
├── .env.copy
├── .gitignore
├── .python-version
├── Dockerfile
├── README.md
├── get_lib_version.py
├── pyproject.toml
├── requirements.txt
└── scrapper_ui.py
```

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository at [https://github.com/klan86at/ecomm-prod-coordinator.git](https://github.com/klan86at/ecomm-prod-coordinator.git)
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

## 📄 License

This project is open source. See the [LICENSE](LICENSE) file for details.
