from datetime import datetime, timezone
from uuid import uuid4
import nbformat
from .engines import papermill_engines
from .exceptions import PapermillMissingParameterException
from .iorw import read_yaml_file
from .log import logger
from .translators import translate_parameters
from .utils import find_first_tagged_cell_index

def add_builtin_parameters(parameters):
    """Add built-in parameters to a dictionary of parameters

    Parameters
    ----------
    parameters : dict
       Dictionary of parameters provided by the user
    """
    pass

def parameterize_path(path, parameters):
    """Format a path with a provided dictionary of parameters

    Parameters
    ----------
    path : string or nbformat.NotebookNode or None
       Path with optional parameters, as a python format string. If path is a NotebookNode
       or None, the path is returned without modification
    parameters : dict or None
       Arbitrary keyword arguments to fill in the path
    """
    pass

def parameterize_notebook(nb, parameters, report_mode=False, comment='Parameters', kernel_name=None, language=None, engine_name=None):
    """Assigned parameters into the appropriate place in the input notebook

    Parameters
    ----------
    nb : NotebookNode
       Executable notebook object
    parameters : dict
       Arbitrary keyword arguments to pass as notebook parameters
    report_mode : bool, optional
       Flag to set report mode
    comment : str, optional
        Comment added to the injected cell
    """
    pass
