import logging
import os
import warnings
from contextlib import contextmanager
from functools import wraps
from .exceptions import PapermillParameterOverwriteWarning
logger = logging.getLogger('papermill.utils')

def any_tagged_cell(nb, tag):
    """Whether the notebook contains at least one cell tagged ``tag``?

    Parameters
    ----------
    nb : nbformat.NotebookNode
        The notebook to introspect
    tag : str
        The tag to look for

    Returns
    -------
    bool
        Whether the notebook contains a cell tagged ``tag``?
    """
    pass

def nb_kernel_name(nb, name=None):
    """Helper for fetching out the kernel name from a notebook object.

    Parameters
    ----------
    nb : nbformat.NotebookNode
        The notebook to introspect
    name : str
        A provided name field

    Returns
    -------
    str
        The name of the kernel or an empty string if none is found
    """
    pass

def nb_language(nb, language=None):
    """Helper for fetching out the programming language from a notebook object.

    Parameters
    ----------
    nb : nbformat.NotebookNode
        The notebook to introspect
    language : str
        A provided language field

    Returns
    -------
    str
        The programming language of the notebook

    Raises
    ------
    ValueError
        If no notebook language is found or provided
    """
    pass

def find_first_tagged_cell_index(nb, tag):
    """Find the first tagged cell ``tag`` in the notebook.

    Parameters
    ----------
    nb : nbformat.NotebookNode
        The notebook to introspect
    tag : str
        The tag to look for

    Returns
    -------
    nbformat.NotebookNode
        Whether the notebook contains a cell tagged ``tag``?
    """
    pass

def merge_kwargs(caller_args, **callee_args):
    """Merge named argument.

    Function takes a dictionary of caller arguments and callee arguments as keyword arguments
    Returns a dictionary with merged arguments. If same argument is in both caller and callee
    arguments the last one will be taken and warning will be raised.

    Parameters
    ----------
    caller_args : dict
        Caller arguments
    **callee_args
        Keyword callee arguments

    Returns
    -------
    args : dict
       Merged arguments
    """
    pass

def remove_args(args=None, **kwargs):
    """Remove arguments from kwargs.

    Parameters
    ----------
    args : list
        Argument names to remove from kwargs
    **kwargs
        Arbitrary keyword arguments

    Returns
    -------
    kwargs : dict
       New dictionary of arguments
    """
    pass

def retry(num):
    pass

@contextmanager
def chdir(path):
    """Change working directory to `path` and restore old path on exit.

    `path` can be `None` in which case this is a no-op.
    """
    pass
