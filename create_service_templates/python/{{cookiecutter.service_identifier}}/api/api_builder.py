from forge.core.api.base import BaseAPI
from forge.core.api.callbacks import Future
from forge.core.api.decorators import api_interface

from services import {{cookiecutter.service_identifier}}
from .api import Result


@api_interface
class {{cookiecutter.service_name_camel_case}}API(BaseAPI):
    service_id = {{cookiecutter.service_identifier}}.SERVICE_ID

    @staticmethod
    def do_something(someData: str) -> Future[Result]:  # TODO: change this
        """Does something"""  # TODO: write some documentation
