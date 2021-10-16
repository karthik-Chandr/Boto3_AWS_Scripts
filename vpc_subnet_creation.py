import boto3


# This is a script which creates a VPC, followed by Subnet.
# If we try to print response and response1, the output would be in JSON format.

# VPC creation
def vpc_creation(resource, region_name):
    client = boto3.client(resource, region_name)
    cidr_block = input("***********Please enter the CIDR for your VPC*********** \n")
    global vpc_id
    response = client.create_vpc(
        CidrBlock=cidr_block,
        TagSpecifications=[
            {
                'ResourceType': 'vpc',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': input("***********Enter the name for your VPC*********** \n")
                    },
                ]
            },
        ]
    )

    print("***********Your VPC has been Successfully created, VPC id is,", response['Vpc']['VpcId'], "***********")
    vpc_id = response['Vpc']['VpcId']


# creating subnets

def subnet_creation(resource, region_name, vpc_id_1):
    cidr_block = input("***********Please enter the CIDR for your Subnet*********** \n")
    client = boto3.client(resource, region_name)
    response1 = client.create_subnet(
        TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': input("***********Enter the name for your Subnet*********** \n")
                    },
                ]
            },
        ],

        VpcId=vpc_id,
        CidrBlock=cidr_block
    )
    sub_id = response1['Subnet']['SubnetId']
    print("Successfully created, subnet id is", sub_id)


vpc_creation('ec2', "us-west-1")
subnet_creation('ec2', "us-west-1", vpc_id)
