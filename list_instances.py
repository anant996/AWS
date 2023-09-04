import boto3 

# Create an EC2 resource 

ec2_resource = boto3.resource('ec2') 

# List all EC2 instances 

for instance in ec2_resource.instances.all(): 

    		print(instance.id, instance.state) 
