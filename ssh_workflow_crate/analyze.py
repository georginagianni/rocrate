import pandas as pd
import spacy
from pathlib import Path
from provenance import record_execution

# Base paths
base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / "data" / "speeches.csv"
output_dir = base_dir / "outputs"
wordcount_path = output_dir / "word_counts.csv"
entities_path = output_dir / "entities.csv"
pos_path = output_dir / "pos_tags.csv"

# Ensure output folder exists
output_dir.mkdir(parents=True, exist_ok=True)

record_execution("Starting spaCy-enhanced text analysis workflow")

# Load data
data = pd.read_csv(data_path)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

all_words = []
all_entities = []
all_pos = []

for row_id, text in enumerate(data["text"], start=1):
    doc = nlp(text)

    # Word counts
    all_words.extend([token.text for token in doc if token.is_alpha])

    # Named entities
    for ent in doc.ents:
        all_entities.append({
            "row_id": row_id,
            "text": ent.text,
            "label": ent.label_
        })

    # POS tags
    for token in doc:
        if token.is_alpha:
            all_pos.append({
                "row_id": row_id,
                "token": token.text,
                "lemma": token.lemma_,
                "pos": token.pos_
            })

# Save word counts
word_counts = pd.Series(all_words).value_counts().reset_index()
word_counts.columns = ["text", "count"]
word_counts.to_csv(wordcount_path, index=False)

# Save entities
entities_df = pd.DataFrame(all_entities)
entities_df.to_csv(entities_path, index=False)

# Save POS tags
pos_df = pd.DataFrame(all_pos)
pos_df.to_csv(pos_path, index=False)

record_execution("spaCy workflow completed successfully")

print("spaCy-enhanced analysis complete")
print(f"Word counts written to: {wordcount_path}")
print(f"Entities written to: {entities_path}")
print(f"POS tags written to: {pos_path}")
