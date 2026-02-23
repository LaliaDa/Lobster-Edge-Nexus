import torch
from transformers import AutoModel, AutoTokenizer

class EmbeddingEngine:
    def __init__(self, model_name="BAAI/bge-large-en-v1.5"):
        
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        print(f"Embedding Engine initialized on {self.device}")

    def generate_vector(self, text_content: str):
        inputs = self.tokenizer(text_content, return_tensors="pt", padding=True, truncation=True).to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).cpu().numpy()