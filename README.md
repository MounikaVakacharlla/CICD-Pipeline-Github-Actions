CI/CD Pipeline using GitHub Actions
Task Overview

This task demonstrates the implementation of a Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions.
The pipeline automates the process of testing, building, deploying, and verifying the application whenever changes are pushed to the repository or a pull request is created.
step1:
Repository Setup

The repository was created and cloned locally using Git.

The following task files and folders were added:

.github/workflows/ci.yml
app.py
requirements.txt
setup.py
tests/test_app.py
README.md

Workflow Configuration

The workflow configuration file was created inside:

.github/workflows/ci.yml

Step2:

The pipeline is automatically triggered on the following GitHub events:

push → Runs whenever code is pushed to the repository
pull_request → Runs whenever a pull request is opened or updated

step3:

Runner Environment

The workflow uses a GitHub-hosted Ubuntu virtual machine environment.

runs-on: ubuntu-latest

This provides a Linux-based environment for executing all CI/CD pipeline stages.

step4:

Python Environment Setup

The workflow configures Python automatically using GitHub Actions.

- name: Setup Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.11'
Install Project Dependencies

The pipeline installs all required project dependencies from the requirements.txt file.

- name: Install Dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt

This step ensures all required packages are available before testing and deployment.

step5:

Run Unit Tests

A testing stage was added using pytest.

- name: Run Tests
  run: pytest tests/

Purpose of this step:

Executes unit tests automatically
Validates application functionality
Prevents deployment if tests fail

step6:

Build Application

The workflow packages the Python application using the following command:

- name: Build Application
  run: python setup.py sdist

Purpose of this step:

Creates a distributable source package
Simulates the application build process
Verifies packaging functionality

Step7:

Deploy to Staging Environment

The deployment stage was configured using SSH into an AWS EC2 instance.

The workflow uses the GitHub Action:

uses: appleboy/ssh-action@v1.0.3

Deployment configuration:

- name: Deploy to EC2
  uses: appleboy/ssh-action@v1.0.3
  with:
    host: ${{ secrets.EC2_HOST }}
    username: ${{ secrets.EC2_USER }}
    key: ${{ secrets.EC2_SSH_KEY }}
    script: |
      cd /project-directory
      git pull origin main
      pip install -r requirements.txt
      sudo systemctl restart application
EC2 Deployment Requirements
AWS EC2 Instance

A running Linux EC2 instance was used as the staging server.

SSH Key Pair

A .pem private key file was generated while creating the EC2 instance.

GitHub Repository Secrets

The following GitHub repository secrets were configured:

Secret Name	Purpose
EC2_HOST	EC2 public IP address
EC2_USER	EC2 instance username
EC2_SSH_KEY	SSH private key content
EMAIL_USERNAME	Sender email username
EMAIL_PASSWORD	Sender email password or app password

Secrets were added in:

GitHub Repository → Settings → Secrets and Variables → Actions
Security Group Configuration

The EC2 Security Group was configured to allow SSH access.

Port	Purpose
22	SSH Access

This enables secure remote deployment from GitHub Actions.

Deployment Process

The deployment step performs the following actions automatically:

Connects securely to the EC2 instance using SSH
Navigates to the project directory
Pulls the latest code from GitHub
Installs updated dependencies
Restarts the application service

This automates the deployment process after successful testing and build stages.

step8:

Smoke Testing

A smoke test stage was added to verify deployment success.

Purpose of smoke testing:

Sends a request to the deployed application
Verifies that the application is responding correctly
Stops the workflow automatically if the application is unavailable

Example smoke test step:

- name: Smoke Test
  run: |
    echo "Running smoke tests..."

step9:

Email Notifications

Email notifications were configured to monitor pipeline execution status.

Purpose of notifications:

Monitor workflow execution
Receive deployment success/failure updates
Identify testing or deployment issues quickly
Improve deployment tracking and visibility

Example notification step:

- name: Send Email Notification
  if: always()
  uses: dawidd6/action-send-mail@v3

///overall workflow

Code Push / Pull Request
            ↓
Install Dependencies
            ↓
Run Unit Tests
            ↓
Build Application
            ↓
Deploy to EC2 Staging Server
            ↓
Run Smoke Tests
            ↓
Send Email Notifications