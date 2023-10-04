import boto3
import json

def lambda_handler(event, context):
    #print(event)
    src = event['currentIntent']['slots']['source']
    dst = event['currentIntent']['slots']['destination']
    
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    graphTable = dynamodb.Table('graph')
    
    response = None
    try:
        path_key  = src + '-' + dst
        path = graphTable.get_item(Key={'path': path_key})['Item']

        response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": path['distance']
            },
        }
    }
    except Exception as e:
        print(f'Error: {e}')
        response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": "Error in getting distance"
            },
        }
    }
    
    print(f'response: {response}')
    return response