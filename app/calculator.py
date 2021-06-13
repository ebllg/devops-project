import json
import time
from typing import Any, Dict


def add(event: Dict[str, Any], context) -> Dict[str, Any]:
    data: dict = json.loads(event["body"])
    result: int = data["num1"] + data["num2"]
    body: str = json.dumps({"sum": result})
    time.sleep(1)
    return {"statusCode": 200, "body": body}
