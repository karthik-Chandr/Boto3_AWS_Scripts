import boto3


# A small script to get the IAM users, User creation date and Last password used
# If we try to print response, the output would be in JSON format.

def iamUser_listing(resource, region_name):
    client = boto3.client(resource, region_name)
    response = client.get_user()
    print("**********UserName is", response['User']['UserName'], "**********")
    print("**********User created date is", response['User']['CreateDate'], "**********")
    print("**********User used his password last on", response['User']['PasswordLastUsed'], "**********")


iamUser_listing('iam', "us-west-1")
