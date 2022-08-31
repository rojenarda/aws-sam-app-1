import json
import boto3

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    try:
        dynamodb = boto3.resource("dynamodb")
        print("Getting the table.")
        table = dynamodb.Table("sam-table")

        print("Formatting request body.")
        item = json.loads(event["body"])

        print("Adding data to the table.")
        table.put_item(Item=item)
        print("Added data to the table.")
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "Error": str(e).replace("\n", "").replace("\\", "")
            }),
        }
        
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Done",
            # "location": ip.text.replace("\n", "")
        }),
    }
