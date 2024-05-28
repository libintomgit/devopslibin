import boto3

regions = ["us-east-1", "us-west-1", "us-west-2", "eu-west-1", "eu-central-1"]

def describe_instances(region):
    ec2 = boto3.client('ec2', region_name=region)
    responses = ec2.describe_instances()

    instances=[]
    for reservation in responses['Reservations']:
        for instance in reservation['Instances']:
            instance_info = {
                'InstanceId': instance.get('InstanceId'),
                'InstanceType': instance.get('InstanceType'),
                'State': instance.get('State', {}).get('Name'),
                'PublicIpAddress': instance.get('PublicIpAddress'),
                'PrivateIpAddress': instance.get('PrivateIpAddress'),
                'AvailabilityZone': instance.get('Placement', {}).get('AvailabilityZone')
            }
            instances.append(instance_info)
    
    return instances

for region in regions:
    print(f"Listing instances in region: {region}")
    instances = describe_instances(region)

    if instances:
        for instance in instances:
            print(f"InstanceId: {instance['InstanceId']}, InstanceType: {instance['InstanceType']}, "
                  f"State: {instance['State']}, PublicIpAddress: {instance['PublicIpAddress']}, "
                  f"PrivateIpAddress: {instance['PrivateIpAddress']}, AvailabilityZone: {instance['AvailabilityZone']}")
    else:
        print("No instances found.")
    print("")



