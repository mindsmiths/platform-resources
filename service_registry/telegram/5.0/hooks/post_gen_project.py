import os
import shutil

from forge.utils.templating import render
from forge_cli.utils import load_yaml, dump_yaml, Secrets, ProjectXML


def setup():
    token = input('Your bot token (from BotFather): ')
    agent = input('Which agent will handle messages?: ')

    # Update config
    config_update = load_yaml(CONFIG_UPDATE)
    with open('../config/config.yaml', 'r') as f:
        data = load_yaml(f.read())
        data['services'].update(config_update)

        if 'telegram-adapter' not in data['services']['rule-engine'].get('dependencies', []):
            data['services']['rule-engine']['dependencies'] = [
                *data['services']['rule-engine'].get('dependencies', []),
                'telegram-adapter'
            ]
    dump_yaml(data, '../config/config.yaml')

    # Update secrets
    if not os.path.exists("../.env"):
        with open("../.env", 'x'):
            pass
    secrets = Secrets.load('../.env')
    secrets.add_blank_line()
    secrets['TELEGRAM_BOT_TOKEN'] = token
    secrets.dump('../.env', '../.env.example')

    # Update pom.xml
    project_xml = ProjectXML("../services/rule_engine/pom.xml")
    project_xml.add_xml_dependency({
        "groupId": "com.mindsmiths",
        "artifactId": "telegram-adapter-client",
        "version": '{{cookiecutter._service_version}}'
    })

    # Update signals.yaml
    if agent:
        signal_path = "../services/rule_engine/src/main/resources/config/signals.yaml"

        os.makedirs(os.path.dirname(signal_path), exist_ok=True)
        if not os.path.exists(signal_path):
            with open(signal_path, 'x'):
                pass
        with open(signal_path, 'r') as f:
            yaml_update = load_yaml(render(SIGNAL_UPDATE, {"agent": agent}))
            if yaml := load_yaml(f.read()):
                yaml.update(yaml_update)
            else:
                yaml = yaml_update
        dump_yaml(yaml, signal_path)

    shutil.rmtree('../{{cookiecutter._service_name}}')


SIGNAL_UPDATE = """
com.mindsmiths.telegramAdapter.events.TelegramReceivedMessage:
  - !GetOrCreateAgentByConnection
    connectionName: telegram
    connectionField: chatId
    agentType: agents.{{'{{agent}}'}}
"""

CONFIG_UPDATE = """
telegram-adapter:
  type: python
  version: {{cookiecutter._service_version}}
  db:
    mongo: true
  env:
    TELEGRAM_BOT_TOKEN: "{{ '{{env.TELEGRAM_BOT_TOKEN}}' }}"
  resources:
    cpu: 81m
    memory: 130Mi
"""

if __name__ == '__main__':
    setup()
