import faiss
import numpy as np
from .vector_store import VectorStore

class FaissStore(VectorStore):
    def __init__(self, index_file='apple_notes_vectors.index'):
        self.index_file = index_file

    def store(self, vectors):
        dimension = vectors[0].shape[0]
        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(vectors))
        faiss.write_index(index, self.index_file)

    def load(self):
        return faiss.read_index(self.index_file)