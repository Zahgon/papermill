import re

class AwsError(Exception):
    """Raised when an AWS Exception is encountered."""

class FileExistsError(AwsError):
    """Raised when a File already exists on S3."""

class PapermillException(Exception):
    """Raised when an exception is encountered when operating on a notebook."""

class PapermillMissingParameterException(PapermillException):
    """Raised when a parameter without a value is required to operate on a notebook."""

class PapermillExecutionError(PapermillException):
    """Raised when an exception is encountered in a notebook."""

    def __init__(self, cell_index, exec_count, source, ename, evalue, traceback):
        args = (cell_index, exec_count, source, ename, evalue, traceback)
        self.cell_index = cell_index
        self.exec_count = exec_count
        self.source = source
        self.ename = ename
        self.evalue = evalue
        self.traceback = traceback
        super().__init__(*args)

    def __str__(self):
        message = f"\n{75 * '-'}\n"
        message += f'Exception encountered at "In [{self.exec_count}]":\n'
        message += strip_color('\n'.join(self.traceback))
        message += '\n'
        return message

class PapermillRateLimitException(PapermillException):
    """Raised when an io request has been rate limited"""

class PapermillOptionalDependencyException(PapermillException):
    """Raised when an exception is encountered when an optional plugin is missing."""

class PapermillWarning(Warning):
    """Base warning for papermill."""

class PapermillParameterOverwriteWarning(PapermillWarning):
    """Callee overwrites caller argument to pass down the stream."""
_COLORS = re.compile('\x1b\\[(K|.*?m)')

def strip_color(text):
    """Remove most ANSI color and style sequences from a string

    Based on https://pypi.org/project/ansicolors/."""
    pass

def missing_dependency_generator(package, dep):
    pass

def missing_environment_variable_generator(package, env_key):
    pass
