import re
import pandas as pd

INPUT="data/raw/Variantesdialectales.txt"
OUTPUT="data/processed/translation_pairs.csv"

rows=[]

with open(INPUT,encoding="utf-8") as f:

    for line in f:

        parts=line.strip().split("|")

        if len(parts)==3:

            fe=parts[0].strip()
            fr=parts[1].strip()
            en=parts[2].strip()

            rows.append([fe,fr,en])

df=pd.DataFrame(rows,columns=["fe","fr","en"])

df.to_csv(OUTPUT,index=False)

print("Extracted",len(df),"rows")
