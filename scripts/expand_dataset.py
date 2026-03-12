import pandas as pd

df=pd.read_csv("data/processed/translation_pairs.csv")

rows=[]

for _,r in df.iterrows():

    fe=r["fe"]
    fr=r["fr"]
    en=r["en"]

    rows.append([fr,fe])
    rows.append([en,fe])
    rows.append([fe,fr])
    rows.append([fe,en])

expanded=pd.DataFrame(rows,columns=["input","output"])

expanded.to_csv("data/processed/augmented_dataset.csv",index=False)

print("Expanded dataset:",len(expanded))
