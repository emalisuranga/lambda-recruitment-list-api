
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('RecruitmentIistSheet')

def lambda_handler(event, context):
    try:
        # Extract parameters from the event
        cn_id = event['queryStringParameters']['cn_id']
        status = event['queryStringParameters']['status']

        # Query the DynamoDB table using the provided parameters
        response = table.get_item(
            Key={
                'cn_id': cn_id,
                'status': status
            }
        )

        # Check if the item was found
        if 'Item' in response:
            # Construct the response with CORS headers
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',  # Replace with your allowed origins
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',  # Add your allowed methods
                },
                'body': json.dumps(response['Item'])
            }
        else:
            # Return a 404 Not Found response with CORS headers
            return {
                'statusCode': 404,
                'headers': {
                    'Access-Control-Allow-Origin': '*',  # Replace with your allowed origins
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',  # Add your allowed methods
                },
                'body': 'Item not found'
            }

    except Exception as e:
        # Handle any errors that occur during execution
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Replace with your allowed origins
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',  # Add your allowed methods
            },
            'body': str(e)
        }
