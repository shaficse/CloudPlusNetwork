import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError


# Initialize the Cognito Identity Provider client
client = boto3.client('cognito-idp', region_name='your-region')

# Replace these variables with your own values
region = 'us-east-1'
user_pool_id = 'us-east-1_hSL7PVXdP'
client_id = '9utv2i7iubja3lsd41nd3oct1'
username = 'shaficse'
password = 'Abc1234!'

# Initialize the Cognito Identity Provider client
client = boto3.client('cognito-idp', region_name=region)

try:
    # Attempt to authenticate the user
    response = client.admin_initiate_auth(
        UserPoolId=user_pool_id,
        ClientId=client_id,
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        }
    )

    # Extract the JWT token from the response
    id_token = response['AuthenticationResult']['IdToken']
    access_token = response['AuthenticationResult']['AccessToken']
    refresh_token = response['AuthenticationResult'].get('RefreshToken')

    print("ID Token:", id_token)
    print("Access Token:", access_token)
    if refresh_token:
        print("Refresh Token:", refresh_token)

except (NoCredentialsError, PartialCredentialsError) as e:
    print("Credentials error:", e)
except ClientError as e:
    print("AWS Client error:", e)