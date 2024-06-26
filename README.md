# vectorizing_apple_notes
Building vector database out of Apple Notes to be used for RAG application

## Repository Structure
```
project_root/
    │
    ├── src/
    │   ├── __init__.py
    │   ├── extractors/
    │   │   ├── __init__.py
    │   │   └── apple_notes_extractor.py
    │   ├── preprocessors/
    │   │   ├── __init__.py
    │   │   └── text_preprocessor.py
    │   ├── vectorizers/
    │   │   ├── __init__.py
    │   │   └── transformer_vectorizer.py
    │   ├── storage/
    │   │   ├── __init__.py
    │   │   ├── vector_store.py
    │   │   └── faiss_store.py
    │   └── config.py
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_apple_notes_extractor.py
    │   ├── test_text_preprocessor.py
    │   ├── test_transformer_vectorizer.py
    │   └── test_faiss_store.py
    │
    ├── .github/
    │   └── workflows/
    |
    ├── containers/
    │   ├── Dockerfile
    │   ├── docker-compose.yml
    │   └── requirements.txt
    │
    ├── poetry.lock
    ├── pyproject.toml
    ├── makefile
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── .env-example
    ├── main.py
    └── README.md
```
TODO: Add a feature to convert .md apple notes to SQLite to mock the apple notes database
TODO: Adapt main and extractor to read from the toy database
