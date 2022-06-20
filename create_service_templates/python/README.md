# Creating a Python service

## How to use
```shell
$ forge create-service -d python
```

## Parameters
- `service_name` - Name of the service in a human-readable format (eg. "WhatsApp Adapter"). Try to keep it short and clear.
- `service_name_camel_case` - Used for class names. A good default will automatically be generated, and you can just press enter to accept it in most cases.
- `service_identifier` - Used for package/file names, and in service communication. A good default will automatically be generated, and you can just press enter to accept it in most cases.
- `service_artifact_name` - Used in config. A good default will automatically be generated, and you can just press enter to accept it in most cases.


## Writing the logic
You can write the service's logic in `services/<new_service>/<new_service>.py`.

You'll see an example function that receives some data, and returns a result. This function is already exposed through an API.
Feel free to change this example and add new functions.

If you don't want to expose any functions, but want some code to be run in a loop instead, just override the `start` function:
```python
class NewService(BaseService):

    def start(self) -> None:
        while True:
            """ TODO: WRITE YOUR MAGIC HERE """
            sleep(5)

```

If you want both, just add `self.start_async_message_consumer()` before the loop in the `start` method, to enable the service to listen to requests in a separate thread.


## Defining an API
To allow other services to communicate with our new service, we'll create a client for them. The `create-service` command already generated some examples for us.

The platform will do most of the work for us, so all we need to do is define the prototypes of the exposed functions in `services/<new_service>/api/api_builder.py`.
Keep in mind that if you're using additional data models in the calls or in the return (eg. `Result` in the example), they *must* be defined somewhere in the `services/<new_service>/api/` package, because this is the only package other services can access.
This also means you *cannot* import any files outside this package in any file defined inside it.

Notice that there is no `self` argument, and that we specify the expected result as _Future[dataType]_ in `api_builder.py`.
This reminds us that the service doesn't wait for the result before continuing. All service communication in the platform is *asynchronous*.

### Java client
The code for handling communication with Java-based services (e.g. Rule Engine) is in the directories under the `services/<new_service>/clients/java` path. 
The generated files also contain template code for API calls. Just mirror what you defined in the Python API, but in Java.

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

You need to run `forge install` from the terminal to finish connecting the services after adding the dependency.


## Service configuration
If you'd like to be able to configure parts of the logic, a good practice is to use settings. Settings are also great for secret values like passwords and authentication tokens.

Settings are regular Python variables, but their values are loaded from environment variables.
To define one, first create `services/<new_service>/settings.py` and add the following code:
```python
from environs import Env

env = Env()
```
Now you can add settings below, here are some examples:
```python
DEFAULT_TIMEZONE = env.str('DEFAULT_TIMEZONE', 'Europe/Zagreb')
HTTP_PORT = env.int('HTTP_PORT', 8080)
AUTH_TOKEN = env.str('AUTH_TOKEN')
USE_WEBHOOK = env.bool('USE_WEBHOOK', True)
```
To override the service defaults, or provide values for settings with no defaults, go to `config/config.yaml` and add something like this to for your service:
```yaml
  new-service:
    ...
    env:
      MY_SERVICE_PORT: 8081
      AUTH_TOKEN: "{{env.NEW_SERVICE_AUTH_TOKEN}}"  # this will read the '.env' file and the system env, and fill it here (good for secrets)
    ...     
```
