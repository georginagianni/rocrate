import json
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("logs/execution_log.json")

def record_execution(message, input_file=None):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "message": message,
        "input_file": input_file
    }

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    if LOG_PATH.exists():
        data = json.loads(LOG_PATH.read_text())
    else:
        data = []

    data.append(entry)
    LOG_PATH.write_text(json.dumps(data, indent=2))
