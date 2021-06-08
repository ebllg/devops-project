from unittest import TestCase

from app.calculator import add

import json


class CalculatorTests(TestCase):
    def test_add(self):
        data = {"num1": 5, "num2": 10}
        event = {"body": json.dumps(data)}

        resp = add(event, context={})

        self.assertEqual(resp["statusCode"], 200)
        self.assertEqual(resp["body"], json.dumps({"latestResult": 15}))
