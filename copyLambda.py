mport boto3
import json

s3 = boto3.resource('s3')

def lambda_handler (event, context):
 bucket = s3.Bucket('sourced-bucket70')
 dest_bucket=s3.Bucket('modfied-bucket70')

 print(dest_bucket)
 print(bucket)
 
 for obj in bucket.objects.filter(Delimiter='/'):
  dest_key=obj.key
  print(dest_key)
  print('copy file ' + dest_key)
  s3.Object(dest_bucket.name, dest_key).copy_from(CopySource= {'Bucket': obj.bucket_name, 'Key': obj.key})
