import json


def add(event, context):
    data = json.loads(event["body"])
    body = {"result": data["num1"] + data["num2"]}
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
