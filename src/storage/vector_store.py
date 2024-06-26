from abc import ABC, abstractmethod

class VectorStore(ABC):
    @abstractmethod
    def store(self, vectors):
        pass

    @abstractmethod
    def load(self):
        pass