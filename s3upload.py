import boto3

s3 = boto3.client('s3')

bucket_name = "blockislandbucket"
file_name = "compressed_data1.gz"

s3.upload_file("compressed_data1.gz", bucket_name, file_name)

