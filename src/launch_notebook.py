from pathlib import Path
import subprocess
import sys


def check_required_files(crate_path: Path) -> None:
    required_files = [
        crate_path / "data" / "speeches.csv",
        crate_path / "notebooks" / "analysis.ipynb",
        crate_path / "environment.yml",
        crate_path / "codemeta.json",
        crate_path / "ro-crate-metadata.json",
    ]

    missing = [str(f) for f in required_files if not f.exists()]
    if missing:
        print("Missing required files:")
        for f in missing:
            print(f" - {f}")
        sys.exit(1)


def run_notebook(crate_path: Path) -> None:
    print(f"Launching notebook from crate: {crate_path}")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "notebooks/analysis.ipynb",
            "--output",
            "executed_analysis.ipynb",
        ],
        cwd=str(crate_path),
        capture_output=True,
        text=True,
    )

    print("STDOUT:")
    print(result.stdout)

    if result.stderr:
        print("STDERR:")
        print(result.stderr)

    if result.returncode != 0:
        print(f"Notebook execution failed with exit code {result.returncode}")
        sys.exit(result.returncode)

    print("Notebook executed successfully.")


if __name__ == "__main__":
    crate_dir = Path("ssh_workflow_crate")
    check_required_files(crate_dir)
    run_notebook(crate_dir)
