import sys
from os import path

from forge_cli.utils import load_templated_yaml


if path.isdir("../services/{{ cookiecutter.service_identifier }}"):
    sys.exit("A service with this identifier already exists")

with open("../config/config.yaml", "r") as f:
    data = load_templated_yaml(f.read())
    if '{{ cookiecutter.service_artifact_name }}' in data['services']:
        sys.exit("A service with this identifier already exists")
