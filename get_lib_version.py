import importlib.metadata
packages = [
    "langchain",
    "langchain-core",
    "python-dotenv"
]

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} is not installed.")

    
