from pathlib import Path
import nbformat
from .engines import papermill_engines
from .exceptions import PapermillExecutionError
from .inspection import _infer_parameters
from .iorw import get_pretty_path, load_notebook_node, local_file_io_cwd, write_ipynb
from .log import logger
from .parameterize import add_builtin_parameters, parameterize_notebook, parameterize_path
from .utils import chdir

def execute_notebook(input_path, output_path, parameters=None, engine_name=None, request_save_on_cell_execute=True, prepare_only=False, kernel_name=None, language=None, progress_bar=True, log_output=False, stdout_file=None, stderr_file=None, start_timeout=60, report_mode=False, cwd=None, **engine_kwargs):
    """Executes a single notebook locally.

    Parameters
    ----------
    input_path : str or Path or nbformat.NotebookNode
        Path to input notebook or NotebookNode object of notebook
    output_path : str or Path or None
        Path to save executed notebook. If None, no file will be saved
    parameters : dict, optional
        Arbitrary keyword arguments to pass to the notebook parameters
    engine_name : str, optional
        Name of execution engine to use
    request_save_on_cell_execute : bool, optional
        Request save notebook after each cell execution
    autosave_cell_every : int, optional
        How often in seconds to save in the middle of long cell executions
    prepare_only : bool, optional
        Flag to determine if execution should occur or not
    kernel_name : str, optional
        Name of kernel to execute the notebook against
    language : str, optional
        Programming language of the notebook
    progress_bar : bool, optional
        Flag for whether or not to show the progress bar.
    log_output : bool, optional
        Flag for whether or not to write notebook output to the configured logger
    start_timeout : int, optional
        Duration in seconds to wait for kernel start-up
    report_mode : bool, optional
        Flag for whether or not to hide input.
    cwd : str or Path, optional
        Working directory to use when executing the notebook
    **kwargs
        Arbitrary keyword arguments to pass to the notebook engine

    Returns
    -------
    nb : NotebookNode
       Executed notebook object
    """
    pass

def prepare_notebook_metadata(nb, input_path, output_path, report_mode=False):
    """Prepare metadata associated with a notebook and its cells

    Parameters
    ----------
    nb : NotebookNode
       Executable notebook object
    input_path : str
        Path to input notebook
    output_path : str
       Path to write executed notebook
    report_mode : bool, optional
       Flag to set report mode
    """
    pass
ERROR_MARKER_TAG = 'papermill-error-cell-tag'
ERROR_STYLE = 'style="color:red; font-family:Helvetica Neue, Helvetica, Arial, sans-serif; font-size:2em;"'
ERROR_MESSAGE_TEMPLATE = f"""<span {ERROR_STYLE}>An Exception was encountered at '<a href="#papermill-error-cell">In [%s]</a>'.</span>"""
ERROR_ANCHOR_MSG = f'<span id="papermill-error-cell" {ERROR_STYLE}>Execution using papermill encountered an exception here and stopped:</span>'

def remove_error_markers(nb):
    pass

def raise_for_execution_errors(nb, output_path):
    """Assigned parameters into the appropriate place in the input notebook

    Parameters
    ----------
    nb : NotebookNode
       Executable notebook object
    output_path : str
       Path to write executed notebook
    """
    pass
