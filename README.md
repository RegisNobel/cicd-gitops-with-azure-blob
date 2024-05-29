YouTube Downloader with Flask, Azure Blob Storage, GitHub Actions, and Kubernetes
This project is a YouTube downloader web application built with Flask, integrated with Azure Blob Storage for storing downloaded videos. It includes a CI/CD pipeline configured with GitHub Actions and deployment automation using Kubernetes.


Table of Contents
Overview
Features
Installation
Usage
CI/CD Pipeline
Kubernetes Deployment
Contributing
License
Overview
The application allows users to input a YouTube video URL, downloads the video, and uploads it to Azure Blob Storage. The CI/CD pipeline ensures continuous integration and deployment, leveraging GitHub Actions and Kubernetes for automation.


Features
Flask Web Application: Simple UI to input YouTube video URL and download video.
Azure Blob Storage: Stores downloaded videos securely.
CI/CD Pipeline: Automates build, test, and deployment processes using GitHub Actions.
Kubernetes Deployment: Deploys the application in a scalable manner using Kubernetes and git ops.


Installation
Prerequisites
Python 3.11
Azure account with Blob Storage setup
Docker
Kubernetes cluster
GitHub account


Setup
Clone the repository:


sh
Copy code
git clone [GitHub Repository URL]
cd [repository-name]
Install dependencies:


sh
Copy code
pip install -r requirements.txt
Set up environment variables. Create a .env file with the following content:


makefile
Copy code
azConnectionString=your_azure_connection_string
Run the Flask application:


sh
Copy code
python app.py


Usage
Navigate to http://localhost:5002 in your web browser.
Enter a YouTube video URL and click "Download".
The video will be downloaded and uploaded to Azure Blob Storage.


CI/CD Pipeline
The CI/CD pipeline is configured using GitHub Actions. It includes the following steps:

Build Docker Image: Builds and pushes the Docker image to Azure Container Registry.
Update Kubernetes Manifests: Updates the image tag in Kubernetes deployment manifests and pushes changes to the repository.


GitHub Actions Workflow
The CI/CD pipeline is defined in the GitHub Actions workflow file: GitHub Actions Workflow File.


Git Ops Deployment
The application is deployed using git ops and Kubernetes. The manifests include a Deployment and a Service for the Flask application.


Source Files
Flask Application (app.py)
GitHub Actions Workflow File
Kubernetes Deployment Manifest
Kubernetes Service Manifest
Dockerfile
Update Script (updatek8s.sh)


Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements.
