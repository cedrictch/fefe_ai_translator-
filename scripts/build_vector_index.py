from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss
import numpy as np

model=SentenceTransformer("all-MiniLM-L6-v2")

df=pd.read_csv("data/processed/augmented_dataset.csv")

sentences=df["input"].tolist()

emb=model.encode(sentences)

index=faiss.IndexFlatL2(384)

index.add(np.array(emb))

faiss.write_index(index,"data/embeddings/vector.index")
