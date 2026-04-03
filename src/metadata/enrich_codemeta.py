
import json
from pathlib import Path


def load_codemeta(path="tools/flat/codemeta_flat.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def enrich_metadata(data: dict) -> dict:
    enriched = data.copy()

    # 1. Add execution command if missing
    if "executionCommand" not in enriched:
        enriched["executionCommand"] = "python src/analyze.py"

    # 2. Normalize software requirements
    if isinstance(enriched.get("softwareRequirements"), list):
        enriched["softwareRequirements"] = [
            req.lower() for req in enriched["softwareRequirements"]
        ]

    # 3. Add dataset reference if missing
    if "dataset" not in enriched:
        enriched["dataset"] = {
            "path": "data/speeches.csv",
            "type": "local"
        }

    # 4. Add environment hints
    enriched["environment"] = {
        "memory": "2GB",
        "cpu": "2 cores"
    }

    return enriched


def save_enriched(data: dict, path="codemeta_enriched.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    codemeta = load_codemeta()
    enriched = enrich_metadata(codemeta)

    save_enriched(enriched)

    print("\n=== Enriched CodeMeta Created ===")
    print("Saved as codemeta_enriched.json")
