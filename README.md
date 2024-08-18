# CI/CD Generator

**Author:** [Siegfried SEKKAI](https://github.com/yourusername)
**Version:** 1.0.0
**License:** MIT

## Overview

**CI/CD Generator** is an advanced tool designed to automate the creation of CI/CD pipelines tailored to specific project needs. This generator analyzes the structure of your repository and automatically creates workflows for various deployment scenarios, including infrastructure provisioning with Terraform, Kubernetes deployments with Helm, configuration management with Ansible, and Docker-based deployments via SSH.

## Features

- **Terraform Support:** Automatically generates workflows for initializing, formatting, and applying Terraform configurations, ensuring your infrastructure is consistently deployed across environments.
- **Kubernetes Deployments:** Detects Helm manifests and generates Kubernetes deployment workflows, making it easy to manage applications in a containerized environment.
- **Ansible Integration:** Generates workflows for running Ansible playbooks, enabling configuration management and application deployment across your infrastructure.
- **Docker SSH Deployments:** Connects to remote VMs via SSH, installs Docker if necessary, and deploys Docker containers, perfect for edge deployments or legacy systems.
- **Modular and Extensible:** Built with flexibility in mind, the generator can be extended to support additional tools and deployment scenarios as needed.

## Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Templates](#templates)
- [Secrets Management](#secrets-management)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with the CI/CD Generator, clone the repository and configure your environment:

```bash
git clone https://github.com/yourusername/ci-cd-generator.git
cd ci-cd-generator
```

Ensure you have Python 3.x installed along with the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Installation

To install and set up the CI/CD Generator:

1. Clone the repository.
2. Install the required Python packages using `pip`.
3. Prepare your repository for the generator by structuring your infrastructure and deployment files accordingly.

## Usage

The generator is designed to be run directly within your repository. It detects specific directory structures and generates the corresponding CI/CD workflows automatically.

### Running the Generator

Simply run the script:

```bash
python scripts/generate_pipeline.py
```

### Supported Scenarios

- **Terraform Modules:** The generator will look for directories containing `main.tf` files and create a workflow to manage your Terraform infrastructure.
- **Helm Manifests:** If a `manifests` directory is detected, the generator will create a Helm deployment workflow.
- **Ansible Playbooks:** The presence of an `ansible` directory triggers the creation of a workflow to run your Ansible playbooks.
- **Docker SSH Deployments:** By setting the `DOCKER_SSH_DEPLOYMENT` environment variable to `true`, the generator will create a workflow for deploying Docker containers to a remote VM via SSH.

### Example Commands

```bash
# Generate workflows for Terraform, Helm, Ansible, and Docker deployments
python scripts/generate_pipeline.py

# Run only Docker SSH deployment workflow generation
DOCKER_SSH_DEPLOYMENT=true python scripts/generate_pipeline.py
```

## Templates

The generator uses Jinja2 templates to create workflows. These templates are stored in the `templates/` directory and can be customized to fit your specific needs.

### Available Templates

- **terraform_template.yml:** Generates workflows for Terraform modules.
- **helm_template.yml:** Creates workflows for deploying applications to Kubernetes using Helm.
- **ansible_template.yml:** Builds workflows for running Ansible playbooks.
- **docker_ssh_template.yml:** Generates workflows for Docker-based deployments via SSH.

## Secrets Management

For secure deployments, the generator requires certain secrets to be configured in your GitHub repository:

- **AWS_ROLE:** IAM role to assume for Terraform and Helm deployments.
- **AWS_REGION:** The AWS region where your resources are deployed.
- **SSH_PRIVATE_KEY:** Private SSH key for connecting to remote VMs.
- **SSH_USER:** SSH username for remote access.
- **SSH_HOST:** Hostname or IP address of the remote VM.
- **DOCKER_IMAGE:** Docker image to be deployed.

These secrets must be added to your repository under "Settings" > "Secrets and variables" > "Actions".

## Contributing

We welcome contributions to the CI/CD Generator project. If you have ideas for new features, templates, or improvements, please open an issue or submit a pull request. For significant changes, please discuss them with the repository maintainers first.

### How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a comprehensive overview of your project, guiding users through installation, usage, and contributions. It emphasizes professionalism and encourages collaboration, which is essential for open-source projects.