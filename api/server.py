from fastapi import FastAPI
from scripts.translate import translate

app=FastAPI()

@app.get("/translate")

def translate_api(text:str):

    return {"translation":translate(text)}
