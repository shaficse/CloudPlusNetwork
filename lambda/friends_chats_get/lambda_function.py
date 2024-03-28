# import json
# import boto3
# from boto3.dynamodb.conditions import Key


# def lambda_handler(event, context):
#     print('input event..')
#     print(event)
    
#     sender_receiver = event['sender_receiver']
#     client = boto3.resource('dynamodb')
#     table           = client.Table('friends_chats')
    
#     #--query --- 
#     response = table.query(
#         KeyConditionExpression = Key('sender_receiver').eq(sender_receiver)
#         )
        
#     print(response)
#     items = response('Items')

#     return items
    
import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    print('input event..')
    print(event)
    
    sender_receiver = event['sender_receiver']
    client = boto3.resource('dynamodb')
    table = client.Table('friends_chats')
    
    #--query --- 
    response = table.query(
        KeyConditionExpression=Key('sender_receiver').eq(sender_receiver)
    )
        
    print(response)
    items = response['Items']  # Corrected this line

    return items
