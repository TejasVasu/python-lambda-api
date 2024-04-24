from . import health_check

# This is the entrypoint for all request, routes it to the appropriate controllers
def lambda_handler(event, context):
    path = event['path']
    print(path)
    if path == '/health/api':
        return health_check.api_health_check(event, context)
    elif path == '/health/dynamo':
        return health_check.dynamo_health_check(event, context)
    else:
        return {
            'statusCode': 404,
            'body': 'Not Found'
        }