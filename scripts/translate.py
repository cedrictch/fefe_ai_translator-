import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

vector=faiss.read_index("data/embeddings/vector.index")

model_emb=SentenceTransformer("all-MiniLM-L6-v2")

df=pd.read_csv("data/processed/augmented_dataset.csv")

tokenizer=AutoTokenizer.from_pretrained("model/nllb_finetuned")
model=AutoModelForSeq2SeqLM.from_pretrained("model/nllb_finetuned")

def translate(text):

    emb=model_emb.encode([text])

    D,I=vector.search(emb,1)

    candidate=df.iloc[I[0][0]]["output"]

    if candidate:
        return candidate

    inputs=tokenizer(text,return_tensors="pt")

    out=model.generate(**inputs)

    return tokenizer.decode(out[0],skip_special_tokens=True)
