"""Utilities for working with S3."""
import logging
import os
import threading
import zlib
from boto3.session import Session
from .exceptions import AwsError
from .utils import retry
logger = logging.getLogger('papermill.s3')

class Bucket:
    """
    Represents a Bucket of storage on S3

    Parameters
    ----------
    name : string
        name of the bucket
    service : string, optional (Default is None)
        name of a service resource, such as SQS, EC2, etc.

    """

    def __init__(self, name, service=None):
        self.name = name
        self.service = service

    def list(self, prefix='', delimiter=None):
        """Limits a list of Bucket's objects based on prefix and delimiter."""
        pass

class Prefix:
    """
    Represents a prefix used in an S3 Bucket.

    Parameters
    ----------
    bucket : object
        A bucket of S3 storage
    name : string
        name of the bucket
    service : string, optional (Default is None)
        name of a service resource, such as SQS, EC2, etc.

    """

    def __init__(self, bucket, name, service=None):
        self.bucket = Bucket(bucket, service=service)
        self.name = name
        self.is_prefix = True
        self.service = service

    def __str__(self):
        return f's3://{self.bucket.name}/{self.name}'

    def __repr__(self):
        return self.__str__()

class Key:
    """
    A key that represents a unique object in an S3 Bucket.

    Represents a file or stream.

    Parameters
    ----------
    bucket : object
        A bucket of S3 storage
    name : string
        representative name of the bucket
    size : ???, optional (Default is None)
    etag : ???, optional (Default is None)
    last_modified : date, optional (Default is None)
    storage_class : ???, optional (Default is None)
    service : string, optional (Default is None)
        name of a service resource, such as SQS, EC2, etc.

    """

    def __init__(self, bucket, name, size=None, etag=None, last_modified=None, storage_class=None, service=None):
        self.bucket = Bucket(bucket, service=service)
        self.name = name
        self.size = size
        self.etag = etag
        if last_modified:
            try:
                self.last_modified = f"{last_modified.isoformat().split('+')[0]}.000Z"
            except ValueError:
                self.last_modified = last_modified
        self.storage_class = storage_class
        self.is_prefix = False
        self.service = service

    def __str__(self):
        return f's3://{self.bucket.name}/{self.name}'

    def __repr__(self):
        return self.__str__()

class S3:
    """
    Wraps S3.

    Parameters
    ----------
    keyname : TODO

    Methods
    -------
    The following are wrapped utilities for S3:
        - cat
        - cp_string
        - list
        - list_dir
        - read

    """
    s3_session = (None, None, None)
    lock = threading.RLock()

    def __init__(self, keyname=None, *args, **kwargs):
        with self.lock:
            if not all(S3.s3_session):
                session = Session()
                client = session.client('s3')
                session_params = {}
                endpoint_url = os.environ.get('BOTO3_ENDPOINT_URL', None)
                if endpoint_url:
                    session_params['endpoint_url'] = endpoint_url
                s3 = session.resource('s3', **session_params)
                S3.s3_session = (session, client, s3)
        (self.session, self.client, self.s3) = S3.s3_session

    def _bucket_name(self, bucket):
        pass

    def _clean(self, name):
        pass

    def _clean_s3(self, name):
        pass

    def _get_key(self, name):
        pass

    def _key_name(self, name):
        pass

    @retry(3)
    def _list(self, prefix='', bucket=None, delimiter=None, keys=False, objects=False, page_size=1000, **kwargs):
        pass

    def _put(self, source, dest, num_callbacks=10, policy='bucket-owner-full-control', **kwargs):
        pass

    def _put_string(self, source, dest, num_callbacks=10, policy='bucket-owner-full-control', **kwargs):
        pass

    def _is_s3(self, name):
        pass

    def cat(self, source, buffersize=None, memsize=2 ** 24, compressed=False, encoding='UTF-8', raw=False):
        """
        Returns an iterator for the data in the key or nothing if the key
        doesn't exist. Decompresses data on the fly (if compressed is True
        or key ends with .gz) unless raw is True. Pass None for encoding to
        skip encoding.

        """
        pass

    def cp_string(self, source, dest, **kwargs):
        """
        Copies source string into the destination location.

        Parameters
        ----------
        source: string
            the string with the content to copy
        dest: string
            the s3 location
        """
        pass

    def list(self, name, iterator=False, **kwargs):
        """
        Returns a list of the files under the specified path
        name must be in the form of `s3://bucket/prefix`

        Parameters
        ----------
        keys: optional
           if True then this will return the actual boto keys for files
           that are encountered
        objects: optional
           if True then this will return the actual boto objects for
           files or prefixes that are encountered
        delimiter: optional
           if set this
        iterator: optional
           if True return iterator rather than converting to list object

        """
        pass

    def listdir(self, name, **kwargs):
        """
        Returns a list of the files under the specified path.

        This is different from list as it will only give you files under the
        current directory, much like ls.

        name must be in the form of `s3://bucket/prefix/`

        Parameters
        ----------
        keys: optional
            if True then this will return the actual boto keys for files
            that are encountered
        objects: optional
            if True then this will return the actual boto objects for
            files or prefixes that are encountered

        """
        pass

    def read(self, source, compressed=False, encoding='UTF-8'):
        """
        Iterates over a file in s3 split on newline.

        Yields a line in file.

        """
        pass
