import json
from src.services import dynamo_db_client


def api_health_check(event, context):
    body = {"message": "API is reachable"}
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response


def dynamo_health_check(event, context):
    resp = dynamo_db_client.table_exists()
    if resp:
        status_code = 200
        msg = "Dynamo DB connection successful"
    else:
        status_code = 500
        msg = "Unable to connect to Dynamo DB"
    body = {"message": msg}
    response = {
        "statusCode": status_code,
        "body": json.dumps(body)
    }

    return response


def dynamo_db_put_item(event, context):
    query_params = event['queryStringParameters']
    id = query_params.get('id')
    name = query_params.get('name')
    resp = dynamo_db_client.put_item(id, name)

    response = {
        "statusCode": 200,
        "body": json.dumps(resp)
    }

    return response

