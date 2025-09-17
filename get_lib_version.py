import importlib.metadata
packages = [
    "langchain",
    "langchain-core",
    "python-dotenv",
    "beautifulsoup4",
    "fastapi",
    "html5lib",
    "jinja2",
    "langchain-astradb",
    "langchain-google-genai",
    "langchain-groq",
    "lxml",
    "python-multipart",
    "selenium",
    "streamlit",
    "undetected-chromedriver",
    "uvicorn",
    "structlog",
    "langgraph",
    "ragas"
]

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} is not installed.")

    
