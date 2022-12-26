
import boto3

#Instances
Ids=['i-01f2b06f0bb44b046' , 'i-0428cdfe81928631d' , 'i-009afda57de57ba5d']

ec2 = boto3.resource("ec2")

x = ec2.instances.filter(InstanceIds=Ids).stop()

print("Instance Stopped")
print(x)
