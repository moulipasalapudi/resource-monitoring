import boto3
# Create an AWS session using default credentials
session = boto3.Session()

# Create an ECR client using the session
ecr_client = session.client('ecr')




# Create a new ECR repository
repository_name = 'cloud-native-repo'
response = ecr_client.create_repository(repositoryName=repository_name)

# Print the repository URI
repository_uri = response['repository']['repositoryUri']
print(repository_uri)