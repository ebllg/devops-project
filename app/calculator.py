import json

from typing import Dict, Any


def add(event: Dict[str, Any], context) -> Dict[str, Any]:
    data: dict = json.loads(event["body"])
    result: int = data["num1"] + data["num2"]
    body: str = json.dumps({"result": result})

    return {"statusCode": 200, "body": body}
