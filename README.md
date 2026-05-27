# CICD-Pipeline-Github-Actions
Firstly i create repo and clone it.
i add some file  are app.py requiremets.txt, setup.py, under the test folder test_app.py and .gitignore/workflow/ci.yml files are added.

The workflow is configured to run automatically on the following events:

push → Executes the workflow whenever code is pushed to the repository.
pull_request → Executes the workflow whenever a pull request is opened or updated.

The workflow uses GitHub-hosted Ubuntu runner environment.

runs-on: ubuntu-latest

This provides a Linux-based virtual machine for executing workflow jobs.

The workflow was updated to install Python and the required project dependencies automatically during the CI process.
A Python environment is configured using the `actions/setup-python` action.
Project dependencies are installed.
This command reads all required packages from the requirements.txt file and installs them in the workflow environment.

A testing step was added to the CI workflow to automatically execute unit tests during the pipeline execution.
The workflow uses `pytest` to run all test cases inside the `tests/` directory.

- name: Run tests
  run: pytest tests/

  A build step was added to package the Python application during the CI workflow execution.

### Build Package
The workflow uses the following command to create a source distribution package.
This command generates a distributable source package for the application.

A simulated deployment step was added to represent the deployment stage in the CI/CD pipeline.

Deploy to Staging Using SSH into EC2

The deployment stage was configured to connect to an EC2 instance using SSH and deploy the latest application code.

Deployment Step
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

The following components are required for deployment:

AWS EC2 Instance

A running Linux EC2 instance in Amazon Web Services using Amazon EC2.

SSH Key Pair

A .pem private key file generated while creating the EC2 instance.

GitHub Secrets

The following repository secrets were configured:

Secret Name	Purpose
EC2_HOST	EC2 public IP address
EC2_USER	EC2 username
EC2_SSH_KEY	SSH private key content
Security Group Configuration

Port 22 (SSH) was enabled in the EC2 Security Group to allow secure remote connections.

Deployment Process Explanation

The deployment step performs the following actions:

Connects securely to the EC2 instance using SSH
Navigates to the project directory
Pulls the latest code from the GitHub repository
Installs updated dependencies
Restarts the application service

This automates the application deployment process after successful build and testing.

The smoke test performs a basic validation of the deployed application by sending an HTTP request to the staging server.

Workflow Actions
Sends a request to the deployed application
Verifies that the server responds successfully
Stops the workflow automatically if the application is unavailable

Purpose of Email Notifications

The email notification step helps:

Monitor CI/CD pipeline execution
Receive workflow success or failure updates
Quickly identify deployment or testing issues
Improve deployment visibility and tracking
GitHub Secrets Configuration

The following secrets were added in GitHub repository settings:

Secret Name	Purpose
EMAIL_USERNAME	Sender email username
EMAIL_PASSWORD	Sender email password or app password