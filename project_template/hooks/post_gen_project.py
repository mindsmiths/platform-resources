import shutil


if __name__ == "__main__":
    shutil.copy('.env.example', '.env')

    print("Project {{cookiecutter.project_name}} was successfully created!")
