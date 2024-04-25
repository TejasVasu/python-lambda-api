import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')
table_name = 'dynamo-test-table'


def table_exists():
    try:
        dynamodb.describe_table(TableName=table_name)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            return False


def put_item(id, name):
    response = dynamodb.put_item(
        TableName=table_name,
        Item={
            'id': {'S': id},
            'name': {'S': name}
            }
        )

    return response
