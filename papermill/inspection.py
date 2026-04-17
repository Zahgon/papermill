"""Deduce parameters of a notebook from the parameters cell."""
from pathlib import Path
import click
from .iorw import get_pretty_path, load_notebook_node, local_file_io_cwd
from .log import logger
from .parameterize import add_builtin_parameters, parameterize_path
from .translators import papermill_translators
from .utils import any_tagged_cell, find_first_tagged_cell_index, nb_kernel_name, nb_language

def _open_notebook(notebook_path, parameters):
    pass

def _infer_parameters(nb, name=None, language=None):
    """Infer the notebook parameters.

    Parameters
    ----------
    nb : nbformat.NotebookNode
        Notebook

    Returns
    -------
    List[Parameter]
       List of parameters (name, inferred_type_name, default, help)
    """
    pass

def display_notebook_help(ctx, notebook_path, parameters):
    """Display help on notebook parameters.

    Parameters
    ----------
    ctx : click.Context
        Click context
    notebook_path : str
        Path to the notebook to be inspected
    """
    pass

def inspect_notebook(notebook_path, parameters=None):
    """Return the inferred notebook parameters.

    Parameters
    ----------
    notebook_path : str or Path
        Path to notebook
    parameters : dict, optional
        Arbitrary keyword arguments to pass to the notebook parameters

    Returns
    -------
    Dict[str, Parameter]
       Mapping of (parameter name, {name, inferred_type_name, default, help})
    """
    pass
