
# Fe'efe'e French Translator

French → Fe'efe'e translation project.

Dataset expected in:

data/dataset/

Files:
01_subject_pronouns.jsonl
02_direct_object_pronouns.jsonl
03_indirect_object_pronouns.jsonl
04_tonic_pronouns.jsonl
05_reflexive_pronouns.jsonl
06_possessive_pronouns.jsonl
07_greetings_and_basic_phrases.jsonl
manual_expressions.jsonl
combined_training_dataset.csv


Full Pipeline Execution

Run these in order:

python scripts/parse_variants_file.py
python scripts/expand_dataset.py
python scripts/train_translation_model.py
python scripts/build_vector_index.py

Then launch UI:

streamlit run web/app.py

Run API:
uvicorn api.server:app --reload

Run UI:
streamlit run web/app.py
# fefe_ai_translator-
