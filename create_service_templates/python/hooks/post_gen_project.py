import shutil

from forge_cli.utils import get_templated_yaml_loader

yaml = get_templated_yaml_loader()

# Inject service's config in the config/config.yaml
with open('../config/config.yaml', 'r') as f:
    config = yaml.load(f.read())

config['services']['{{cookiecutter.service_artifact_name}}'] = {
    "type": "python",
    "db": {
        "mongo": True,
    },
    "resources": {
        "cpu": "100m",
        "memory": "100Mi"
    }
}

with open('../config/config.yaml', 'w') as f:
    yaml.dump(config, f)

# Move service's directory with its files to project/services
shutil.move('../{{cookiecutter.service_identifier}}', '../services')
print('\n{{cookiecutter.service_name}} was successfully incorporated into your project!')
