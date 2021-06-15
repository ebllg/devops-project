import json
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


def add(event: Dict[str, Any], context) -> Dict[str, Any]:
    data: dict = json.loads(event["body"])

    if not isinstance(data["num1"], int) or not isinstance(data["num2"], int):
        logger.error(f"Invalid operands: {data['num1']}, {data['num2']}")
        return {"statusCode": 400, "body": json.dumps({"error": "Operands must be integers."})}

    result: int = data["num1"] + data["num2"]
    body: str = json.dumps({"sum": result})

    return {"statusCode": 200, "body": body}
