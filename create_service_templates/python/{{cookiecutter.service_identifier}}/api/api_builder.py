from forge.core.api import BaseAPI, Future
from forge.core.api import api_interface

from services import {{cookiecutter.service_identifier}}
from .api import Result


@api_interface
class {{cookiecutter.service_name_camel_case}}API(BaseAPI):
    service_name = {{cookiecutter.service_identifier}}.SERVICE_NAME

    @staticmethod
    def do_something(someData: str) -> Future[Result]:  # TODO: change this
        """Does something"""  # TODO: write some documentation
