import json
from pathlib import Path


REQUIRED_FIELDS = {
    "execution": [
        "codeRepository",
        "programmingLanguage",
        "runtimePlatform",
        "softwareRequirements"
    ],
    "metadata": [
        "name",
        "description",
        "license"
    ],
    "workflow": [
        "input",
        "output"
    ]
}


def load_codemeta(path: str = "codemeta.json") -> dict:
    codemeta_path = Path(path)

    if not codemeta_path.exists():
        raise FileNotFoundError(f"CodeMeta file not found: {codemeta_path}")

    with codemeta_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def check_missing_fields(data: dict):
    print("\n=== Metadata Completeness Check ===\n")

    for category, fields in REQUIRED_FIELDS.items():
        print(f"{category.upper()}:")

        for field in fields:
            if field not in data or not data[field]:
                print(f" Missing: {field}")
            else:
                print(f" Found {field}")

        print()


if __name__ == "__main__":
    codemeta = load_codemeta("codemeta.json")
    check_missing_fields(codemeta)
