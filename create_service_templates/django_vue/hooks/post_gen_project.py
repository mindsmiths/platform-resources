import shutil

from forge_cli.utils import load_yaml, dump_yaml

# Inject service's config in the config/config.yaml
with open('../config/config.yaml', 'r') as f:
    config = load_yaml(f.read())

config['services']['{{cookiecutter.service_artifact_name}}'] = {
    "type": "django",
    "db": {
        "postgres": True,
    },
    "dependencies": [
        "django~=3.2.0",
        "django-environ~=0.7",
        "django-jet-reboot~=1.3.1",
        "psycopg2-binary~=2.9.0",
        "gunicorn~=20.1.0",
    ],
    "env": {
        "DJANGO_SUPERUSER_USERNAME": "admin",
        "DJANGO_SUPERUSER_PASSWORD": "{{'{{'}} env.{{cookiecutter.service_identifier.upper()}}_ADMIN_PASSWORD | default(\"admin\") {{'}}'}}",
        "SITE_URL": "{{'{{'}} \"{{cookiecutter.service_artifact_name}}.\" + env.get(\"HOST_DOMAIN\", \"\") {{'}}'}}",
        "INTERNAL_SITE_URL": "http://{{cookiecutter.service_artifact_name}}",
        "SECRET_KEY": "{{cookiecutter._secret_key}}",
    },
    "resources": {
        "cpu": "100m",
        "memory": "300Mi"
    }
}

dump_yaml(config, '../config/config.yaml')

# Local config
with open('../config/local.config.yaml', 'r') as f:
    local_config = load_yaml(f.read())

if 'services' not in local_config:
    local_config['services'] = {}
local_config['services']['{{cookiecutter.service_artifact_name}}'] = {
    "port": {{cookiecutter.local_port}},
}

dump_yaml(local_config, '../config/local.config.yaml')

# Move service's directory with its files to project/services
shutil.move('../{{cookiecutter.service_identifier}}', '../services')
print('\n{{cookiecutter.service_name}} was successfully incorporated into your project!')
