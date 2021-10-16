import boto3


# This is a script which creates a VPC, followed by Subnet creation and a Route table creation.
# After creating the above, the script will associate the subnet with the Route table.
# If we try to print response, response1 and response2, the output would be in JSON format.

# VPC creation
def vpc_creation(resource, region_name):
    global vpc_id
    global client
    client = boto3.client(resource, region_name)
    cidr_block = input("***********Please enter the CIDR for your VPC*********** \n")
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

def subnet_creation(vpc_id_1):
    global sub_id
    cidr_block = input("***********Please enter the CIDR for your Subnet*********** \n")
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
    print("***********Successfully created, subnet id is", sub_id, "***********")


# creating a route table

def create_routeTable(vpc_id):
    global rt_id
    response2 = client.create_route_table(

        VpcId=vpc_id,
        TagSpecifications=[
            {
                'ResourceType': 'route-table',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': input("***********Enter a name for your Route Table*********** \n")
                    },
                ]
            },
        ]
    )

    rt_id = response2['RouteTable']['RouteTableId']
    print("***********Successfully created, Route table id is", rt_id, "***********")


# RT association

def routeTable_association(sub_id, rt_id):
    rt_a = client.associate_route_table(

        RouteTableId=rt_id,
        SubnetId=sub_id,

    )
    print("***********Successfully attached subnet ", sub_id, "to route table", rt_id, "***********")


vpc_creation('ec2', "us-west-1")
subnet_creation(vpc_id)
create_routeTable(vpc_id)
routeTable_association(sub_id, rt_id)
