import fnmatch
import json
import os
import sys
import warnings
from contextlib import contextmanager
import entrypoints
import nbformat
import requests
import yaml
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential
from .exceptions import PapermillException, PapermillRateLimitException, missing_dependency_generator, missing_environment_variable_generator
from .log import logger
from .utils import chdir
from .version import version as __version__
try:
    from .s3 import S3
except ImportError:
    S3 = missing_dependency_generator('boto3', 's3')
try:
    from .adl import ADL
except ImportError:
    ADL = missing_dependency_generator('azure.datalake.store', 'azure')
except KeyError as exc:
    if exc.args[0] == 'APPDATA':
        ADL = missing_environment_variable_generator('azure.datalake.store', 'APPDATA')
    else:
        raise
try:
    from .abs import AzureBlobStore
except ImportError:
    AzureBlobStore = missing_dependency_generator('azure.storage.blob', 'azure')
try:
    from gcsfs import GCSFileSystem
except ImportError:
    GCSFileSystem = missing_dependency_generator('gcsfs', 'gcs')
try:
    from pyarrow.fs import FileSelector, HadoopFileSystem
except ImportError:
    HadoopFileSystem = missing_dependency_generator('pyarrow', 'hdfs')
try:
    from github import Github
except ImportError:
    Github = missing_dependency_generator('pygithub', 'github')

def fallback_gs_is_retriable(e):
    pass
try:
    try:
        from gcsfs.retry import is_retriable as gs_is_retriable
    except ImportError:
        from gcsfs.utils import is_retriable as gs_is_retriable
except ImportError:
    gs_is_retriable = fallback_gs_is_retriable
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

class PapermillIO:
    """
    The holder which houses any io system registered with the system.
    This object is used in a singleton manner to save and load particular
    named Handler objects for reference externally.
    """

    def __init__(self):
        self.reset()

    def read(self, path, extensions=['.ipynb', '.json']):
        pass

    def write(self, buf, path, extensions=['.ipynb', '.json']):
        pass

    def listdir(self, path):
        pass

    def pretty_path(self, path):
        pass

    def reset(self):
        pass

    def register(self, scheme, handler):
        pass

    def register_entry_points(self):
        pass

    def get_handler(self, path, extensions=None):
        """Get I/O Handler based on a notebook path

        Parameters
        ----------
        path : str or nbformat.NotebookNode or None
        extensions : list of str, optional
            Required file extension options for the path (if path is a string), which
            will log a warning if there is no match. Defaults to None, which does not
            check for any extensions

        Raises
        ------
        PapermillException: If a valid I/O handler could not be found for the input path

        Returns
        -------
        I/O Handler
        """
        pass

class HttpHandler:

    @classmethod
    def read(cls, path):
        pass

    @classmethod
    def listdir(cls, path):
        pass

    @classmethod
    def write(cls, buf, path):
        pass

    @classmethod
    def pretty_path(cls, path):
        pass

class LocalHandler:

    def __init__(self):
        self._cwd = None

    def read(self, path):
        pass

    def listdir(self, path):
        pass

    def write(self, buf, path):
        pass

    def pretty_path(self, path):
        pass

    def cwd(self, new_path):
        """Sets the cwd during reads and writes"""
        pass

class S3Handler:

    @classmethod
    def read(cls, path):
        pass

    @classmethod
    def listdir(cls, path):
        pass

    @classmethod
    def write(cls, buf, path):
        pass

    @classmethod
    def pretty_path(cls, path):
        pass

class ADLHandler:

    def __init__(self):
        self._client = None

    def _get_client(self):
        pass

    def read(self, path):
        pass

    def listdir(self, path):
        pass

    def write(self, buf, path):
        pass

    def pretty_path(self, path):
        pass

class ABSHandler:

    def __init__(self):
        self._client = None

    def _get_client(self):
        pass

    def read(self, path):
        pass

    def listdir(self, path):
        pass

    def write(self, buf, path):
        pass

    def pretty_path(self, path):
        pass

class GCSHandler:
    RATE_LIMIT_RETRIES = 3
    RETRY_DELAY = 1
    RETRY_MULTIPLIER = 1
    RETRY_MAX_DELAY = 4

    def __init__(self):
        self._client = None

    def _get_client(self):
        pass

    def read(self, path):
        pass

    def listdir(self, path):
        pass

    def write(self, buf, path):
        pass

    def pretty_path(self, path):
        pass

class HDFSHandler:

    def __init__(self):
        self._client = None

    def _get_client(self):
        pass

    def read(self, path):
        pass

    def listdir(self, path):
        pass

    def write(self, buf, path):
        pass

    def pretty_path(self, path):
        pass

class GithubHandler:

    def __init__(self):
        self._client = None

    def _get_client(self):
        pass

    def read(self, path):
        pass

    def listdir(self, path):
        pass

    def write(self, buf, path):
        pass

    def pretty_path(self, path):
        pass

class StreamHandler:
    """Handler for Stdin/Stdout streams"""

    def read(self, path):
        pass

    def listdir(self, path):
        pass

    def write(self, buf, path):
        pass

    def pretty_path(self, path):
        pass

class NotebookNodeHandler:
    """Handler for input_path of nbformat.NotebookNode object"""

    def read(self, path):
        pass

    def listdir(self, path):
        pass

    def write(self, buf, path):
        pass

    def pretty_path(self, path):
        pass

class NoIOHandler:
    """Handler for output_path of None - intended to not write anything"""

    def read(self, path):
        pass

    def listdir(self, path):
        pass

    def write(self, buf, path):
        pass

    def pretty_path(self, path):
        pass

class NoDatesSafeLoader(yaml.SafeLoader):
    yaml_implicit_resolvers = {k: [r for r in v if r[0] != 'tag:yaml.org,2002:timestamp'] for (k, v) in yaml.SafeLoader.yaml_implicit_resolvers.items()}
papermill_io = PapermillIO()
papermill_io.register('local', LocalHandler())
papermill_io.register('s3://', S3Handler)
papermill_io.register('adl://', ADLHandler())
papermill_io.register('abs://', ABSHandler())
papermill_io.register('http://', HttpHandler)
papermill_io.register('https://', HttpHandler)
papermill_io.register('gs://', GCSHandler())
papermill_io.register('hdfs://', HDFSHandler())
papermill_io.register('http://github.com/', GithubHandler())
papermill_io.register('https://github.com/', GithubHandler())
papermill_io.register('-', StreamHandler())
papermill_io.register_entry_points()

def read_yaml_file(path):
    """Reads a YAML file from the location specified at 'path'."""
    pass

def write_ipynb(nb, path):
    """Saves a notebook object to the specified path.
    Args:
        nb_node (nbformat.NotebookNode): Notebook object to save.
        notebook_path (str): Path to save the notebook object to.
    """
    pass

def load_notebook_node(notebook_path):
    """Returns a notebook object with papermill metadata loaded from the specified path.

    Args:
        notebook_path (str): Path to the notebook file.

    Returns:
        nbformat.NotebookNode

    """
    pass

def list_notebook_files(path):
    """Returns a list of all the notebook files in a directory."""
    pass

def get_pretty_path(path):
    pass

@contextmanager
def local_file_io_cwd(path=None):
    pass
