import subprocess
import sys

def run_step(command, description):
    print(f"\n=== {description} ===\n")
    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        print(f"Failed: {description}")
        exit(1)

if __name__ == "__main__":
    py = sys.executable

    # Step 1 — Enrich metadata
    run_step(
        f'"{py}" src/metadata/enrich_codemeta.py',
        "Enriching CodeMeta"
    )

    # Step 2 — Build RO-Crate
    run_step(
        f'"{py}" src/crate/build_from_metadata.py',
        "Building RO-Crate from metadata"
    )

    # Step 3 — Execute workflow
    run_step(
        f'"{py}" src/launch_crate.py',
        "Executing workflow"
    )

    print("\nPipeline completed successfully!")
