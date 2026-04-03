from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "data/speeches.csv",
    "src/analyze.py",
    "notebooks/analysis.ipynb",
    "environment.yml",
    "codemeta.json",
    "vocab/vocab.ttl",
    "outputs/word_counts.csv",
    "logs/execution_log.json",
]


def validate_project() -> bool:
    base_dir = Path(__file__).resolve().parent.parent
    missing = []

    for rel_path in REQUIRED_FILES:
        file_path = base_dir / rel_path
        if not file_path.exists():
            missing.append(rel_path)

    if missing:
        print("Project validation failed. Missing required files:")
        for item in missing:
            print(f" - {item}")
        return False

    print("Project validation successful. All required files are present.")
    return True


if __name__ == "__main__":
    validate_project()
