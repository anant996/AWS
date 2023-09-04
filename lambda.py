def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        # Split the object key to extract the directory path and file name
        parts = object_key.split('/')
        file_name = parts[-1]
        file_path = '/'.join(parts[:-1]) if len(parts) > 1 else ''
        
        print(f"Bucket: {bucket_name}")
        print(f"File Name: {file_name}")
        print(f"File Path: {file_path}")
        
        # Your processing logic here
        
    return {
        'statusCode': 200,
        'body': 'Extraction and processing completed.'
    }
