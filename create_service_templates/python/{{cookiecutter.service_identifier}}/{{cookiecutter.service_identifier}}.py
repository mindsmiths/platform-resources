import logging

from forge.conf import settings as forge_settings
from forge.core.api.decorators import api
from forge.core.base import BaseService

from .api import Result

logger = logging.getLogger(forge_settings.DEFAULT_LOGGER)


class {{cookiecutter.service_name_camel_case}}(BaseService):

    @api
    async def do_something(self, someData: str) -> Result:  # TODO: change this
        # This function is automatically called when another service invokes it through the service's API.

        """ TODO: WRITE YOUR MAGIC HERE """

        # Optionally return something which will be sent as a callback signal to the calling service
        # It can be anything that is serializable to JSON (primitive, dict, list, dataclass...)
        return Result(success=True)
