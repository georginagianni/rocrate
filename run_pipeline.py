from pathlib import Path
import subprocess
import sys

from src.validate_project import validate_project


def run_analysis():
    print("\n--- Running analysis workflow ---")

    result = subprocess.run(
        [sys.executable, "src/analyze.py"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)
        raise SystemExit("Analysis workflow failed.")


def build_crate():
    print("\n--- Generating RO-Crate ---")

    result = subprocess.run(
        [sys.executable, "workflow.py"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)
        raise SystemExit("RO-Crate generation failed.")


def main():
    print("\nExecutable SSH Workflow Pipeline\n")

    print("--- Validating project ---")
    if not validate_project():
        raise SystemExit("Validation failed.")

    run_analysis()
    build_crate()

    print("\nPipeline completed successfully.")
    print("RO-Crate generated in: ssh_workflow_crate/")


if __name__ == "__main__":
    main()
