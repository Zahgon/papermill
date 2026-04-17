"""Utilities for working with Azure blob storage"""
import io
import re
from azure.identity import EnvironmentCredential
from azure.storage.blob import BlobServiceClient

class AzureBlobStore:
    """
    Represents a Blob of storage on Azure

    Methods
    -------
    The following are wrapped utilities for Azure storage:
        - read
        - listdir
        - write
    """

    def _blob_service_client(self, account_name, sas_token=None):
        pass

    @classmethod
    def _split_url(self, url):
        """
        see: https://docs.microsoft.com/en-us/azure/storage/common/storage-dotnet-shared-access-signature-part-1
        abs://myaccount.blob.core.windows.net/sascontainer/sasblob.txt?sastoken
        """
        pass

    def read(self, url):
        """Read storage at a given url"""
        pass

    def listdir(self, url):
        """Returns a list of the files under the specified path"""
        pass

    def write(self, buf, url):
        """Write buffer to storage at a given url"""
        pass
