from src.extractors.apple_notes_extractor import AppleNotesExtractor
from src.preprocessors.text_preprocessor import TextPreprocessor
from src.vectorizers.transformer_vectorizer import TransformerVectorizer
from src.storage.faiss_store import FaissStore
from src.config import CONFIG

def main():
    # Extract
    extractor = AppleNotesExtractor(CONFIG['db_path'])
    notes = extractor.extract()

    # Preprocess
    # preprocessor = TextPreprocessor()
    # preprocessed_notes = [preprocessor.preprocess(note) for note in notes]

    # # Vectorize
    # vectorizer = TransformerVectorizer(CONFIG['vector_model'])
    # vectors = vectorizer.vectorize(preprocessed_notes)

    # # Store
    # store = FaissStore(CONFIG['index_file'])
    # store.store(vectors)

    # print(f"Vectorization complete. Vector database saved as '{CONFIG['index_file']}'")

if __name__ == "__main__":
    main()


