# -*- coding: utf-8 -*-
'''
Sandbox settings
'''

from .common import *  # noqa: F403

REPO_SITE_SLUG = '{{cookiecutter.service_identifier}}_sandbox'

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True  # type: ignore # noqa: F405
SECRET_KEY = env('SECRET_KEY', default='{{cookiecutter._secret_key}}')  # noqa: F405

SITE_URL = env('SITE_URL')  # noqa: F405
INTERNAL_SITE_URL = env('INTERNAL_SITE_URL')  # noqa: F405
ALLOWED_HOSTS = ['localhost', SITE_URL.split('//')[-1], INTERNAL_SITE_URL.split('//')[-1]]

MODULE = 'sandbox'
