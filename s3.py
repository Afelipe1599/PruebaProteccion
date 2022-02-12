"""Boto3 Module"""
import boto3


def upload_file(name, bucket,object_name):
    "Function upload files"
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(name,bucket,object_name)
    return response

def download_file(name,bucket):
    "Function download file"
    s3_client = boto3.resource('s3')
    output = f"downloads/{name}"
    s3_client.Bucket(bucket).download_file(name, output)
    return output

def list_file(bucket):
    "Function list files"
    s3_client = boto3.client('s3')
    contents = []
    if 'Contents' in s3_client.list_objects(Bucket=bucket):
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            contents.append(item)
    return contents
