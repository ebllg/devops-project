import json
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


def check_float_or_int(num):
    if isinstance(num, int) or isinstance(num, float):
        return True
    return False


def add(event: Dict[str, Any], context) -> Dict[str, Any]:
    data: dict = json.loads(event["body"])

    if not check_float_or_int(data["num1"]) or not check_float_or_int(data["num2"]):
        logger.error(f"Invalid operands: {data['num1']}, {data['num2']}")
        raise Exception("Operands must be floats or integers!")

    result: int = data["num1"] + data["num2"]
    body: str = json.dumps({"sum": result})

    return {"statusCode": 200, "body": body}
