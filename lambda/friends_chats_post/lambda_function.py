# import json
# import boto3
# from boto3.dynamodb.conditions import Key


# def lambda_handler(event, context):
    
    
   
#     client = boto3.resource('dynamodb')
#     table           = client.Table('friends_chats')
    
#     sender_receiver = event['sender_receiver']
#     unixtime        = event['unixtime']
#     sender          = event['sender']
#     receiver        = event['receiver']
#     message         = event['message']
    
    
#     if sender_receiver:
#         input  = { 'sender_receiver': sender_receiver, 'unixtime':unixtime,
#             'sender':sender, 'receiver':receiver, 'message':message
#         }
        
#         response = table.put_item(Item=input)
        
    
    
#     #--query --- 
#     return response
    
    
    
# import json
# import boto3
# from botocore.exceptions import ClientError

# def lambda_handler(event, context):
#     # Initialize DynamoDB client
#     client = boto3.resource('dynamodb')
#     table = client.Table('friends_chats')

#     # Extract message attributes from the event
#     try:
#         sender_receiver = event['sender_receiver']
#         unixtime = event['unixtime']
#         sender = event['sender']
#         receiver = event['receiver']
#         message = event['message']
#     except KeyError as e:
#         return {
#             'statusCode': 400,
#             'body': json.dumps({'error': f'Missing key: {str(e)}'}),
#             'headers': {'Content-Type': 'application/json'}
#         }

#     # Construct the item to insert into DynamoDB
#     item = {
#         'sender_receiver': sender_receiver,
#         'unixtime': unixtime,
#         'sender': sender,
#         'receiver': receiver,
#         'message': message
#     }

#     # Attempt to insert the item into the DynamoDB table
#     try:
#         response = table.put_item(Item=item)
#         return {
#             'statusCode': 200,
#             'body': json.dumps({'message': 'Message successfully received'}),
#             'headers': {'Content-Type': 'application/json'}
#         }
#     except ClientError as e:
#         return {
#             'statusCode': 500,
#             'body': json.dumps({'error': str(e.response['Error']['Message'])}),
#             'headers': {'Content-Type': 'application/json'}
#         }


import json
import boto3
from botocore.exceptions import ClientError

# Define the JSON schema for validation (as an example, adjust according to your needs)
message_schema = {
    "type": "object",
    "properties": {
        "sender_receiver": {"type": "string"},
        "unixtime": {"type": "integer"},
        "sender": {"type": "string"},
        "receiver": {"type": "string"},
        "message": {"type": "string"}
    },
    "required": ["sender_receiver", "unixtime", "sender", "receiver", "message"]
}

def validate_data(data, schema):
    # Placeholder for JSON schema validation logic.
    # You would typically use a library like jsonschema to validate the data against the schema.
    # This function should return True if the data is valid, and False or raise an exception if not.
    # For simplicity, this example assumes data is always valid.
    return True

def lambda_handler(event, context):
    # Initialize DynamoDB client
    try:
        client = boto3.resource('dynamodb')
        table = client.Table('friends_chats')
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to initialize DynamoDB client'}),
            'headers': {'Content-Type': 'application/json'}
        }

    # Validate incoming event against the schema
    if not validate_data(event, message_schema):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid message format'}),
            'headers': {'Content-Type': 'application/json'}
        }

    # Extract message attributes from the event
    try:
        sender_receiver = event['sender_receiver']
        unixtime = event['unixtime']
        sender = event['sender']
        receiver = event['receiver']
        message = event['message']
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f'Missing key: {str(e)}'}),
            'headers': {'Content-Type': 'application/json'}
        }

    # Construct the item to insert into DynamoDB
    item = {
        'sender_receiver': sender_receiver,
        'unixtime': unixtime,
        'sender': sender,
        'receiver': receiver,
        'message': message
    }

    # Attempt to insert the item into the DynamoDB table
    try:
        response = table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Message successfully received'}),
            'headers': {'Content-Type': 'application/json'}
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e.response['Error']['Message'])}),
            'headers': {'Content-Type': 'application/json'}
        }
