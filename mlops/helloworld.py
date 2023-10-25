import boto3

def loginwebpageWithAWSCognito(username, password):
    # Login to AWS Cognito
    # username = "XXXX"
    # password = "XXXX"
    # cognito_client = boto3.client('cognito-idp', region_name='us-east-1')
    # response = cognito_client.initiate_auth(
    #     ClientId='7q0uq5qbqjfqmhk5k8q0h0qd2',
    #     AuthFlow='USER_PASSWORD_AUTH',
    #     AuthParameters={
    #         'USERNAME': username,
    #         'PASSWORD': password
    #     }
    # )
    # print(response)
    # return response
    return "test"

def login():
    results = loginwebpageWithAWSCognito("XXXX", "XXXX")
    return results

if __name__ == "__main__":
    print(login())
