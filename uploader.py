import boto3

session = boto3.session.Session()
client = session.client('s3',
                        region_name='nyc3',
                        endpoint_url='https://XXXX.nyc3.digitaloceanspaces.com',
                        aws_access_key_id='XXX',
                        aws_secret_access_key='XXX')

client.upload_file('testing.txt',  # Path to local file
                   'folder-name',  # Name of Space folder
                   'testing.txt')  # Name for remote file
