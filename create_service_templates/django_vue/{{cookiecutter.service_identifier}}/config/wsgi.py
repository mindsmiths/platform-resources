"""
WSGI config

"""
import os
import sys

import forge
from django.core.wsgi import get_wsgi_application

# Have both project and service roots in path
if 'services/{{cookiecutter.service_identifier}}' not in os.getcwd():
    sys.path.append(os.getcwd() + '/services/{{cookiecutter.service_identifier}}')
else:
    sys.path.append(os.getcwd().replace('/services/{{cookiecutter.service_identifier}}', ''))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
forge.setup('{{cookiecutter.service_identifier}}')

application = get_wsgi_application()

from service import Service  # noqa: E402
Service().start_in_thread()
