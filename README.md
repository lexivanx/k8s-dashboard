# Kubernetes Security Dashboard

A Kubernetes Security Dashboard that provides a comprehensive overview of the security posture of a Kubernetes cluster. This project monitors the cluster for security best practices and compliance, offering real-time feedback and remediation suggestions. It integrates open-source security tools and custom scripts to automate security checks, providing a single-pane-of-glass view for cluster administrators.

## Features

- Cluster information retrieval using the Kubernetes API
- CIS benchmark assessment using kube-bench
- Pod Security Policy (PSP) violations checking using kube-psp-advisor
- Network policies listing using the Kubernetes API
- Container image scanning using Trivy
- Runtime security monitoring
- Compliance reporting and alerting via email and Slack

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Trivy command-line tool (https://github.com/aquasecurity/trivy#installation)
- Kubernetes cluster access for cluster information retrieval and network policy listing

### Installation

1. Clone the repository:

```git clone git@github.com:lexivanx/k8s-dashboard.git```

2. Change to the project directory:

```cd k8s-dashboard```

3. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

4. Install the required packages:

```pip install -r requirements.txt```

5. Set up the `config/local.yaml` file with your specific configurations (refer to `config/default.yaml` for examples) and add the required API keys, tokens, and credentials for email and Slack alerting.

6. Run the application:

```python app/main.py```

7. Open a web browser and navigate to `http://localhost:5000` to view the dashboard.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
