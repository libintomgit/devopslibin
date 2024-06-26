



### Query All Instance with details.
(InstanceID,InstanceType, State, PublicIpAddress, PrivateIpAddress, Tags, Region with Zone and output to table)

`aws ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId, InstanceType, State.Name, PublicIpAddress, PrivateIpAddress, Tags, Placement.AvailabilityZone]" --output table`