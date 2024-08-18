import os
from jinja2 import Environment, FileSystemLoader

def find_terraform_modules(root_dir):
    terraform_dirs = []
    for root, dirs, files in os.walk(root_dir):
        if 'main.tf' in files:
            terraform_dirs.append(root)
    return terraform_dirs

def has_helm_manifests(root_dir):
    # Vérifie si le dossier 'manifests' existe à la racine du projet
    return os.path.isdir(os.path.join(root_dir, 'manifests'))

def has_ansible_playbooks(root_dir):
    # Vérifie si le dossier 'ansible' existe à la racine du projet
    return os.path.isdir(os.path.join(root_dir, 'ansible'))

def generate_workflow(template_name, output_filename, context, template_dir, output_dir):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)

    output = template.render(context)

    output_path = os.path.join(output_dir, output_filename)
    with open(output_path, 'w') as f:
        f.write(output)

if __name__ == "__main__":
    repo_dir = os.getenv('REPO_DIR', '.')
    template_dir = 'templates'
    output_dir = '.github/workflows'

    # Générer des workflows pour Terraform
    terraform_modules = find_terraform_modules(repo_dir)

    for module in terraform_modules:
        generate_workflow(
            'terraform_template.yml',
            f'{os.path.basename(module)}_terraform.yml',
            {'module_name': os.path.basename(module), 'terraform_directory': module},
            template_dir,
            output_dir
        )

    # Générer un workflow pour Helm s'il y a un dossier 'manifests'
    if has_helm_manifests(repo_dir):
        generate_workflow(
            'helm_template.yml',
            'helm_deployment.yml',
            {'helm_directory': 'manifests'},
            template_dir,
            output_dir
        )

    # Générer un workflow pour Ansible s'il y a un dossier 'ansible'
    if has_ansible_playbooks(repo_dir):
        generate_workflow(
            'ansible_template.yml',
            'ansible_deployment.yml',
            {'ansible_directory': 'ansible', 'playbook': 'site.yml'},
            template_dir,
            output_dir
        )

    # Générer un workflow pour Docker via SSH
    if os.getenv('DOCKER_SSH_DEPLOYMENT') == 'true':
        generate_workflow(
            'docker_ssh_template.yml',
            'docker_ssh_deployment.yml',
            {},
            template_dir,
            output_dir
        )