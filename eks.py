from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Create API instances
apps_v1_api = client.AppsV1Api(api_client)
core_v1_api = client.CoreV1Api(api_client)

# Define the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "flask-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "flask-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-flask-container",
                        image="294452575100.dkr.ecr.us-east-1.amazonaws.com/my_monitoring_app",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ],
                image_pull_secrets=[client.V1LocalObjectReference(name="ecr-secretkey")]
            )
        )
    )
)

# Update the existing deployment
try:
    apps_v1_api.patch_namespaced_deployment(
        name="flask-app",
        namespace="default",
        body=deployment
    )
    print("Deployment updated successfully")
except ApiException as e:
    print(f"Failed to update deployment: {e}")

# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-flask-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "flask-app"},
        ports=[client.V1ServicePort(port=5000, target_port=5000)],
        type="ClusterIP"  # You can use "NodePort" or "LoadBalancer" depending on your use case
    )
)

# Update the existing service
try:
    core_v1_api.patch_namespaced_service(
        name="my-flask-service",
        namespace="default",
        body=service
    )
    print("Service updated successfully")
except ApiException as e:
    print(f"Failed to update service: {e}")
