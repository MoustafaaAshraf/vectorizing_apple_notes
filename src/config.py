import os

CONFIG = {
    'db_path': os.getenv('APPLE_NOTES_DB_PATH'),
    'vector_model': os.getenv('VECTOR_MODEL', 'sentence-transformers/all-MiniLM-L6-v2'),
    'index_file': os.getenv('INDEX_FILE', 'apple_notes_vectors.index'),
}