import json

from typing import Dict, Any
import telnetlib


def add(event: Dict[str, Any], context) -> Dict[str, Any]:
    data: dict = json.loads(event["body"])
    result: int = data["num1"] + data["num2"]
    body: str = json.dumps({"newResult": result})
    eval("2 + 2")
    return {"statusCode": 200, "body": body}
