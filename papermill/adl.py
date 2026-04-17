"""Utilities for working with Azure data lake storage"""
import re
from azure.datalake.store import core, lib

class ADL:
    """
    Represents an Azure Data Lake

    Methods
    -------
    The following are wrapped utilities for Azure storage:
    - read
    - listdir
    - write
    """

    def __init__(self):
        self.token = None

    @classmethod
    def _split_url(cls, url):
        pass

    def _get_token(self):
        pass

    def _create_adapter(self, store_name):
        pass

    def listdir(self, url):
        """Returns a list of the files under the specified path"""
        pass

    def read(self, url):
        """Read storage at a given url"""
        pass

    def write(self, buf, url):
        """Write buffer to storage at a given url"""
        pass
