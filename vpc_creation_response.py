import boto3


# Small example of how VPC can be created using automation within no time.
# If we try to print response, the output would be in JSON format.

# VPC creation
def vpc_creation(resource, region_name):
    client = boto3.client(resource, region_name)
    cidr_block = input("***********Please enter the CIDR for your VPC***********")
    response = client.create_vpc(
        CidrBlock=cidr_block,
        TagSpecifications=[
            {
                'ResourceType': 'vpc',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Project'
                    },
                ]
            },
        ]
    )

    print("***********Your VPC has been Successfully created, VPC id is,", response['Vpc']['VpcId'], "***********")
    # vpc_id = response['Vpc']['VpcId']


vpc_creation('ec2', "us-west-1")
