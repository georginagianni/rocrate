import json
from pathlib import Path
from rocrate.rocrate import ROCrate
from datetime import date


def load_metadata(path="codemeta_enriched.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_crate(metadata: dict):
    crate = ROCrate()

    crate.name = metadata.get("name", "Generated Workflow")
    crate.description = metadata.get("description", "")

    crate.root_dataset["license"] = metadata.get("license", "")
    crate.root_dataset["datePublished"] = date.today().isoformat()

    # Add dataset
    dataset = metadata.get("dataset", {})
    if "path" in dataset:
        crate.add_file(dataset["path"], properties={
            "name": "Input dataset"
        })

    # Add script (from executionCommand)
    exec_cmd = metadata.get("executionCommand", "")
    if "src/analyze.py" in exec_cmd:
        crate.add_file("src/analyze.py", properties={
            "@type": "ComputationalWorkflow",
            "name": "spaCy-enhanced SSH text analysis workflow",
            "description": "Workflow for SSH text analysis using spaCy, producing word counts, named entities, and POS tags.",
            "programmingLanguage": "Python",
            "input": metadata.get("dataset", {}).get("path", ""),
            "output": metadata.get("output", [])
})
        
    # Add provenance module
    crate.add_file("src/provenance.py", properties={
        "name": "Provenance tracking module"
    })

    # Add environment file
    crate.add_file("environment.yml", properties={
        "name": "Execution environment"
    })

    # Add CodeMeta itself
    crate.add_file("codemeta_enriched.json", properties={
        "name": "Enriched metadata"
    })

    # Add tool metadata entities
    if Path("tools/flat/codemeta_flat.json").exists():
        crate.add_file("tools/flat/codemeta_flat.json", properties={
            "@type": "SoftwareSourceCode",
            "name": "FLAT - FoLiA Linguistic Annotation Tool",
            "description": "External SSH annotation tool represented through CodeMeta metadata."
    })

    if Path("tools/spacy/codemeta_spacy.json").exists():
        crate.add_file("tools/spacy/codemeta_spacy.json", properties={
            "@type": "SoftwareSourceCode",
            "name": "spaCy NLP Toolkit",
            "description": "Local executable NLP tool represented through CodeMeta metadata."
    })

    # Add outputs 
    outputs = metadata.get("output", [])
    for out in outputs:
        crate.add_file(out, properties={
            "name": "Workflow output"
        })

    crate.write("ssh_workflow_crate")

    print("\n=== RO-Crate built from metadata ===")


if __name__ == "__main__":
    metadata = load_metadata()
    build_crate(metadata)
