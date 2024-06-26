from transformers import AutoTokenizer, AutoModel
import torch

class TransformerVectorizer:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def vectorize(self, texts):
        vectors = []
        for text in texts:
            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, max_length=512, padding=True)
            with torch.no_grad():
                outputs = self.model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
            vectors.append(embeddings)
        return vectors