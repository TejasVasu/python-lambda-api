import json
from ..services import dynamo_db_client

def api_health_check(event, context):
    body = { "message": "API is reachable" }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def dynamo_health_check(event, context):
    resp = dynamo_db_client.put_item()
    response = {
            "statusCode": 200,
            "body": json.dumps(resp)
        }

    return response
