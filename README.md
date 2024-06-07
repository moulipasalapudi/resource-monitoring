<h1>Cloud Native Resource Monitoring Application</h1>



<h2>Overview</h2>

<p>The Cloud Native Resource Monitoring Application is designed to provide real-time monitoring of system resources in cloud-native environments. It utilizes <code>psutil</code> for collecting system utilization data and is containerized for seamless deployment across various cloud platforms.</p>

<h2>Features</h2>

<ul>
    <li><strong>Real-Time Monitoring:</strong> Monitor CPU, memory, disk, and network utilization in real-time.</li>
    <li><strong>Containerized Deployment:</strong> Easily deploy the application using Docker or Kubernetes.</li>
    <li><strong>Scalability:</strong> Designed to scale effortlessly with your cloud infrastructure.</li>
    <li><strong>Customizable Alerts:</strong> Set customizable alerts for resource thresholds to optimize resource allocation.</li>
</ul>

<h2>Installation</h2>

<h3>Requirements</h3>
<ul>
    <li>Docker installed</li>
    <li>AWS CLI installed and configured</li>
    <li>Boto3 installed</li>
    <li>Kubectl installed and configured</li>
    <li>AWS EKS CLI tools installed</li>
</ul>

<h3>Local Setup</h3>

<ol>
    <li>Clone the repository:</li>
    <pre><code>git clone https://github.com/moulipasalapudi/resource-monitoring.git</code></pre>
    <li>Install dependencies:</li>
    <pre><code>pip install -r requirements.txt</code></pre>
    <li>Run the application:</li>
    <pre><code>python app.py</code></pre>
</ol>

<h3>Docker Deployment</h3>

<ol>
    <li>Build the Docker image:</li>
    <pre><code>docker build -t myapp .</code></pre>
    <li>Run the Docker container:</li>
    <pre><code>docker run -p 5000:5000 myapp</code></pre>
</ol>
h2>Step 1: Create an ECR Repository</h2>
<pre><code>
import boto3

ecr_client = boto3.client('ecr')

repository_name = "my_monitoring_app"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
</code></pre>

<h2>Step 2: Build and Tag Docker Image</h2>
<pre><code>
docker build -t my_monitoring_app .
docker tag my_monitoring_app:latest &lt;repository_uri&gt;:latest
</code></pre>

<h2>Step 3: Push Docker Image to ECR</h2>
<pre><code>
aws ecr get-login-password --region &lt;region&gt; | docker login --username AWS --password-stdin &lt;account_id&gt;.dkr.ecr.&lt;region&gt;.amazonaws.com
docker push &lt;repository_uri&gt;:latest
</code></pre>

<h2>Step 4: Create EKS Cluster</h2>
<pre><code>
eksctl create cluster --name my-cluster --region &lt;region&gt; --nodegroup-name linux-nodes --node-type t2.micro --nodes 3 --nodes-min 1 --nodes-max 4 --managed
</code></pre>

<h2>Step 6: Run the Python Script</h2>
<pre><code>
python eks.py
</code></pre>
<h2>Step 7: Check Pods</h2>
<pre><code>
kubectl get pods
kubectl describe pod &lt;pod_name&gt;
kubectl logs &lt;pod_name&gt;
</code></pre>
<h2>Step 9: Verify Service</h2>
<pre><code>
kubectl get services
kubectl describe service &lt;service-name&gt;
kubectl port-forward service/&lt;service-name&gt;8080:80
</code></pre>

<ol>
    <li>Access the monitoring dashboard at <code>http://localhost:5000</code> (or the respective host and port if deployed elsewhere).</li>
    <li>Navigate through different tabs to view CPU, memory, disk, and network utilization metrics.</li>
    <li>Set up alerts based on specific resource thresholds to receive notifications.</li>
</ol>



</body>
</html>
