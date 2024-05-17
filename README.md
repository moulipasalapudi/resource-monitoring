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
    <li>Python 3.x</li>
    <li>Docker (for containerization)</li>
    <li>Kubernetes (optional, for Kubernetes deployment)</li>
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

<h3>Kubernetes Deployment</h3>

<ol>
    <li>Apply the Kubernetes manifest:</li>
    <pre><code>kubectl apply -f kubernetes-manifest.yaml</code></pre>
</ol>

<h2>Usage</h2>

<ol>
    <li>Access the monitoring dashboard at <code>http://localhost:5000</code> (or the respective host and port if deployed elsewhere).</li>
    <li>Navigate through different tabs to view CPU, memory, disk, and network utilization metrics.</li>
    <li>Set up alerts based on specific resource thresholds to receive notifications.</li>
</ol>

<h2>Contributing</h2>

<p>Contributions are welcome! Feel free to submit pull requests, bug reports, feature requests, or any suggestions to enhance the application.</p>



</body>
</html>
