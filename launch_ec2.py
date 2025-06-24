import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Create a new security group
response = ec2.create_security_group(
    GroupName='MyVedioChatSG',
    Description='Security group for Video Chat App',
    VpcId='your-vpc-id-here'  # Need your VPC ID
)
security_group_id = response['GroupId']

print(f"Created security group with ID: {security_group_id}")

# Set inbound rule to allow HTTP traffic
ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[{
        'IpProtocol': 'tcp',
        'FromPort': 80,
        'ToPort': 80,
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
    }]
)

print("Inbound HTTP rule added")

# Launch an EC2 instance
response = ec2.run_instances(
    ImageId='ami-0c94855ba95c71c99',  # Amazon Linux 2
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-key-name',  # Provide your key pair name
    SecurityGroupIds=[security_group_id],
    SubnetId='your-subnet-id'  # Your subnet ID
)

instance_id = response['Instances'][0]['InstanceId']
print(f"Launched EC2 Instance with ID: {instance_id}")