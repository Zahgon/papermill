import asyncio
import sys
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError
from traitlets import Bool, Instance

class PapermillNotebookClient(NotebookClient):
    """
    Module containing a  that executes the code cells
    and updates outputs
    """
    log_output = Bool(False).tag(config=True)
    stdout_file = Instance(object, default_value=None).tag(config=True)
    stderr_file = Instance(object, default_value=None).tag(config=True)

    def __init__(self, nb_man, km=None, raise_on_iopub_timeout=True, **kw):
        """Initializes the execution manager.

        Parameters
        ----------
        nb_man : NotebookExecutionManager
            Notebook execution manager wrapper being executed.
        km : KernerlManager (optional)
            Optional kernel manager. If none is provided, a kernel manager will
            be created.
        """
        super().__init__(nb_man.nb, km=km, raise_on_iopub_timeout=raise_on_iopub_timeout, **kw)
        self.nb_man = nb_man

    def execute(self, **kwargs):
        """
        Wraps the parent class process call slightly
        """
        pass

    def papermill_execute_cells(self):
        """
        This function replaces cell execution with it's own wrapper.

        We are doing this for the following reasons:

        1. Notebooks will stop executing when they encounter a failure but not
           raise a `CellException`. This allows us to save the notebook with the
           traceback even though a `CellExecutionError` was encountered.

        2. We want to write the notebook as cells are executed. We inject our
           logic for that here.

        3. We want to include timing and execution status information with the
           metadata of each cell.
        """
        pass

    def log_output_message(self, output):
        """
        Process a given output. May log it in the configured logger and/or write it into
        the configured stdout/stderr files.

        :param output: nbformat.notebooknode.NotebookNode
        :return:
        """
        pass

    def process_message(self, *arg, **kwargs):
        pass
