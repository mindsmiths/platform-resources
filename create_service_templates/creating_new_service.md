## Mindsmiths Platform Cookiecutters
Here you can find templates for creating new services on the Mindsmiths Platform. 

Currently, only creating Python and Django services is supported out-of-the-box. 
We plan to add support for more languages in the future, and would be happy to accept any contributions.

What follows is a quick tutorial on how to create a new service on the platform.

### Adding a new service
First, you need to run `forge create-service` in the Terminal. You will be prompted to choose which type of service you want to create.
You can see the [full list of available templates here](https://github.com/mindsmiths/platform-resources/tree/main/create_service_templates).
Make sure you match the exact name of the directory.
```shell
root:/app$ forge create-service
Which type of service would you like to create (eg. python, django)? ... [default: python]:
```
Read the template's documentation to fill in the prompts that follow correctly.
Taking for example a Python service, you next need to set the name for the new service. The name should be capitalized, with words separated by spaces (e.g. `New Service`).
The rest of the naming formats will be automatically generated based on the initial name you choose, so you can just press enter:
```shell
service_name: New Service
service_name_camel_case [NewService]: 
service_identifier [new_service]: 
service_artifact_name [new-service]:

New Service was successfully incorporated into your project!
```

For a Django service, the process is similar:
```shell
Which type of service would you like to create (eg. python, django)? ... [default: python]: django
service_name: New Django Service
service_identifier [new_django_service]: 
service_artifact_name [new-django-service]: 
local_port [8001]:

New Django Service was successfully incorporated into your project!
```

That's it! The added service will now appear in your directory tree, and will be automatically added at the bottom of your `config/config.yaml`, for example:
```yaml
...
  new-service:
    type: python
    db:
      mongo: true
    resources:
      cpu: 100m
      memory: 100Mi
```

Don't forget to run `forge install` to install any new dependencies, and you're good to go!
