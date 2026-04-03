from pathlib import Path
import subprocess
import sys


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    crate_dir = base_dir / "ssh_workflow_crate"
    workflow_script = crate_dir / "analyze.py"
    data_file = crate_dir / "speeches.csv"

    if not crate_dir.exists():
        raise FileNotFoundError(f"Crate directory not found: {crate_dir}")

    if not workflow_script.exists():
        raise FileNotFoundError(
            f"Workflow script not found in crate: {workflow_script}")

    if not data_file.exists():
        raise FileNotFoundError(f"Dataset not found in crate: {data_file}")

    print(f"Launching workflow from crate: {crate_dir.name}")

    result = subprocess.run(
        [sys.executable, str(workflow_script)],
        cwd=crate_dir,
        capture_output=True,
        text=True
    )

    print("STDOUT:")
    print(result.stdout)

    if result.stderr:
        print("STDERR:")
        print(result.stderr)

    if result.returncode != 0:
        raise SystemExit(
            f"Crate execution failed with exit code {result.returncode}")


if __name__ == "__main__":
    main()
