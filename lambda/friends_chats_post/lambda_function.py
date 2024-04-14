 
    
import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Initialize DynamoDB client
    client = boto3.resource('dynamodb')
    table = client.Table('friends_chats')

    # Print the entire event to CloudWatch Logs
    print("Received event:", event)

    # Extract message attributes from the event
    try:
        sender_receiver = event['sender_receiver']
        unixtime = event['unixtime']
        sender = event['sender']
        receiver = event['receiver']
        message = event['message']
        
        # Print extracted values for debugging
        print(f"Sender/Receiver: {sender_receiver}, Unix Time: {unixtime}, Sender: {sender}, Receiver: {receiver}, Message: {message}")

    except KeyError as e:
        print(f"Error: Missing key - {str(e)}") # Printing the missing key error
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
        print("Insert item response:", response) # Printing the response from DynamoDB
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Message successfully received'}),
            'headers': {'Content-Type': 'application/json'}
        }
    except ClientError as e:
        print(f"Error: DynamoDB client error - {str(e.response['Error']['Message'])}") # Printing the DynamoDB error
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e.response['Error']['Message'])}),
            'headers': {'Content-Type': 'application/json'}
        }