## Mindsmiths Platform Cookiecutters
Here you can find templates for creating new services on the Mindsmiths Platform. 

Currently only creating Python and Django services is supported out-of-the-box. 
We plan to add support for more languages in the future, and would be happy to accept any contributions.

What follows is a quick tutorial on how to create a new service on the platform.

### Adding a new service
First, you need to run `forge create_service` in the Terminal. You will be prompted to choose which type of service you want to create.
The only currently supported options with the `create_service` command are Django and Python services:
```shell
root:/app$ forge create-service
Would you like to create a Python [0], or Django [1] service? [0]:
```
Taking for example a Python service, you next need to set the name for the new service. The name should be capitalized, with words separated by spaces (e.g. `New Service`).
The rest of the naming formats will be automatically generated based on the initial name you choose:
```shell
service_name: New Service
service_name_camel_case [NewService]: 
service_identifier [new_service]: 
service_artifact_name [new-service]:

New Service was successfully incorporated into your project!
```

For a Django service, the process is similar:
```shell
Would you like to create a Python [0], or Django [1] service? [0]: 1
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

Now just run `forge install` and you're good to go!

### Service communication
For Python services, the `create_service` command also generates some template files for passing the data between services. The communication between services is defined through APIs.

#### Python API
Since this is a Python service, your newly created service contains the `services/new_service/api` directory with template files for communication with other Python-based services.
You add the code that the service executes on API calls in `services/new_service/new_service.py`. 

The expected result is specified in `services/new_service/api/api_builder.py`. 
Notice that we specify the expected result as _Future[dataType]_. This simply means that the system doesn't wait to receive the result before executing something else, making the service communication asynchronous.


You can additionally create a `services/new_service/api/api.py` file to add classes for the data models you want to use.


#### Java client
The code for handling communication with Java-based services (e.g. Rule Engine) is in the directories under the `services/new_service/clients/java` path. 
The generated files also contain template code for API calls, so the classes can be named however you want, and contain any data and functionalities you want them to.

Note that if you want the new service to communicate with the Rule Engine, you should add it as a dependency to its `pom.xml` (in `services/rule_engine/pom.xml`):
```xml
<dependencies>
    ...
		<dependency>
			<groupId>com.mindsmiths</groupId>
			<artifactId>new-service</artifactId>
			<version>4.0.0a0</version>
		</dependency>
    ...
</dependencies>
```

You need to run `forge install` from the Terminal to finish connecting the services after adding the dependency.


The structure of Django services is somewhat different, but follows the regular structure of Django [apps](https://www.askpython.com/django/django-app-structure-project-structure).


### Setting environment variables
Finally, if your service requires environment variables, create a `services/new_service/settings.py` and add the following code:
```python
from environs import Env

env = Env()


ENV_VARIABLE = env.str('ENV_VARIABLE')
```
After that, go to `config/config.yaml` and add these lines to for your service:
```yaml
  new-service:
    ...
    env:
      ENV_VARIABLE: "{{env.ENV_VARIABLE}}"
    ...     
```
