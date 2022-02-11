"""Boto3 Module"""
import boto3

#Metodo que sube un archivo a S3
def upload_file(name, bucket,object_name):
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(name,bucket,object_name)
    return response

#Metodo que descarga un archivo de S3
def download_file(name,bucket):
    s3 = boto3.resource('s3')
    output = f"downloads/{name}"
    s3.Bucket(bucket).download_file(name, output)
    return output

#Metodo para listar archivos de S3
def list_file(bucket):
    s3_client = boto3.client('s3')
    contents = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            contents.append(item)
        return contents
    except:
        return contents