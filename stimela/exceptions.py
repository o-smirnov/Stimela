# -*- coding: future_fstrings -*-

class StimelaBaseException(Exception):
    def __init__(self, message, log=False):
        Exception.__init__(self, message)
        self.logged = log
        if log:
            from stimela import logger
            logger().error(message)

class SchemaError(StimelaBaseException):
    pass

class DefinitionError(StimelaBaseException):
    pass

class StepValidationError(StimelaBaseException):
    pass

class RecipeValidationError(StimelaBaseException):
    pass

class CabValidationError(StimelaBaseException):
    pass

class ParameterValidationError(StimelaBaseException):
    pass

class StimelaCabParameterError(StimelaBaseException):
    pass

class StimelaRecipeExecutionError(StimelaBaseException):
    pass

class StimelaBaseImageError(StimelaBaseException):
    pass


class PipelineException(StimelaBaseException):
    """ 
    Encapsulates information about state of pipeline when an
    exception occurs
    """

    def __init__(self, exception, completed, failed, remaining):
        message = ("Job '%s' failed: %s" % (failed.label, str(exception)))

        super(PipelineException, self).__init__(message)

        self._completed = completed
        self._failed = failed
        self._remaining = remaining

    @property
    def completed(self):
        return self._completed

    @property
    def failed(self):
        return self._failed

    @property
    def remaining(self):
        return self._remaining

