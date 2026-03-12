from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset
from transformers import Trainer, TrainingArguments

model_name="facebook/nllb-200-distilled-600M"

tokenizer=AutoTokenizer.from_pretrained(model_name)
model=AutoModelForSeq2SeqLM.from_pretrained(model_name)

dataset=load_dataset("csv",data_files="data/processed/augmented_dataset.csv")

def preprocess(example):

    inputs=tokenizer(example["input"],max_length=128,truncation=True)

    targets=tokenizer(example["output"],max_length=128,truncation=True)

    inputs["labels"]=targets["input_ids"]

    return inputs

dataset=dataset.map(preprocess)

args=TrainingArguments(

    output_dir="model/nllb_finetuned",
    per_device_train_batch_size=4,
    num_train_epochs=5,
    save_steps=500
)

trainer=Trainer(
    model=model,
    args=args,
    train_dataset=dataset["train"]
)

trainer.train()
