from abc import ABC, abstractmethod
from cerberus import Validator
from flask import Response


class Action(ABC):

    schema = {}

    def __init__(self, logger):
        self.logger = logger
        self.validator = Validator(purge_unknown=True)

    @abstractmethod
    def action(self, **kwargs) -> Response:
        raise NotImplementedError

    def validate(self, request_data) -> dict:
        validated = {}
        if self._isValid(request_data):
            validated = self.normalized(request_data)
        else:
            raise ValueError(self.validation_error())

        return validated

    def _isValid(self, request_data) -> bool:
        return self.validator.validate(request_data, self.schema)

    def validation_error(self) -> str:
        return "{}: {}".format(
            next(iter(self.validator.errors)),
            next(iter(self.validator.errors.values()))[0],
        )

    def normalized(self, request_data) -> dict:
        return self.validator.normalized(request_data, self.schema)

    def log(self, message: str, type: str = "debug"):
        getattr(self.logger, type)("[{}] {}".format(self.__class__.__name__, message))
