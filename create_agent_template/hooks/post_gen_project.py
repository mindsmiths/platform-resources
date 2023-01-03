import shutil

from forge_cli.config import PROJECT_ROOT

if __name__ == "__main__":
    shutil.move('{{cookiecutter.agent_name_pascal}}.java', PROJECT_ROOT / "services/rule_engine/src/main/java/agents/")
    shutil.move('../{{cookiecutter.agent_name_camel}}', PROJECT_ROOT / "services/rule_engine/src/main/resources/rules/")

    print("Agent {{cookiecutter.agent_name}} created!")
