import logging
import math
import re
import shlex
from .exceptions import PapermillException
from .models import Parameter
logger = logging.getLogger(__name__)

class PapermillTranslators:
    """
    The holder which houses any translator registered with the system.
    This object is used in a singleton manner to save and load particular
    named Translator objects for reference externally.
    """

    def __init__(self):
        self._translators = {}

    def register(self, language, translator):
        pass

    def find_translator(self, kernel_name, language):
        pass

class Translator:

    @classmethod
    def translate_raw_str(cls, val):
        """Reusable by most interpreters"""
        pass

    @classmethod
    def translate_escaped_str(cls, str_val):
        """Reusable by most interpreters"""
        pass

    @classmethod
    def translate_str(cls, val):
        """Default behavior for translation"""
        pass

    @classmethod
    def translate_none(cls, val):
        """Default behavior for translation"""
        pass

    @classmethod
    def translate_int(cls, val):
        """Default behavior for translation"""
        pass

    @classmethod
    def translate_float(cls, val):
        """Default behavior for translation"""
        pass

    @classmethod
    def translate_bool(cls, val):
        """Default behavior for translation"""
        pass

    @classmethod
    def translate_dict(cls, val):
        pass

    @classmethod
    def translate_list(cls, val):
        pass

    @classmethod
    def translate(cls, val):
        """Translate each of the standard json/yaml types to appropriate objects."""
        pass

    @classmethod
    def comment(cls, cmt_str):
        pass

    @classmethod
    def assign(cls, name, str_val):
        pass

    @classmethod
    def codify(cls, parameters, comment='Parameters'):
        pass

    @classmethod
    def inspect(cls, parameters_cell):
        """Inspect the parameters cell to get a Parameter list

        It must return an empty list if no parameters are found and
        it should ignore inspection errors.

        .. note::
            ``inferred_type_name`` should be "None" if unknown (set it
            to "NoneType" for null value)

        Parameters
        ----------
        parameters_cell : NotebookNode
            Cell tagged _parameters_

        Returns
        -------
        List[Parameter]
            A list of all parameters
        """
        pass

class PythonTranslator(Translator):
    PARAMETER_PATTERN = re.compile('^(?P<target>\\w[\\w_]*)\\s*(:\\s*[\\"\']?(?P<annotation>\\w[\\w_\\[\\],\\s]*)[\\"\']?\\s*)?=\\s*(?P<value>.*?)(\\s*#\\s*(type:\\s*(?P<type_comment>[^\\s]*)\\s*)?(?P<help>.*))?$')

    @classmethod
    def translate_float(cls, val):
        pass

    @classmethod
    def translate_bool(cls, val):
        pass

    @classmethod
    def translate_dict(cls, val):
        pass

    @classmethod
    def translate_list(cls, val):
        pass

    @classmethod
    def comment(cls, cmt_str):
        pass

    @classmethod
    def codify(cls, parameters, comment='Parameters'):
        pass

    @classmethod
    def inspect(cls, parameters_cell):
        """Inspect the parameters cell to get a Parameter list

        It must return an empty list if no parameters are found and
        it should ignore inspection errors.

        Parameters
        ----------
        parameters_cell : NotebookNode
            Cell tagged _parameters_

        Returns
        -------
        List[Parameter]
            A list of all parameters
        """
        pass

class RTranslator(Translator):

    @classmethod
    def translate_none(cls, val):
        pass

    @classmethod
    def translate_bool(cls, val):
        pass

    @classmethod
    def translate_dict(cls, val):
        pass

    @classmethod
    def translate_list(cls, val):
        pass

    @classmethod
    def comment(cls, cmt_str):
        pass

    @classmethod
    def assign(cls, name, str_val):
        pass

class ScalaTranslator(Translator):

    @classmethod
    def translate_int(cls, val):
        pass

    @classmethod
    def translate_dict(cls, val):
        """Translate dicts to scala Maps"""
        pass

    @classmethod
    def translate_list(cls, val):
        """Translate list to scala Seq"""
        pass

    @classmethod
    def comment(cls, cmt_str):
        pass

    @classmethod
    def assign(cls, name, str_val):
        pass

class JuliaTranslator(Translator):

    @classmethod
    def translate_none(cls, val):
        pass

    @classmethod
    def translate_dict(cls, val):
        pass

    @classmethod
    def translate_list(cls, val):
        pass

    @classmethod
    def comment(cls, cmt_str):
        pass

class MatlabTranslator(Translator):

    @classmethod
    def translate_escaped_str(cls, str_val):
        """Translate a string to an escaped Matlab string"""
        pass

    @staticmethod
    def __translate_char_array(str_val):
        """Translates a string to a Matlab char array"""
        pass

    @classmethod
    def translate_none(cls, val):
        pass

    @classmethod
    def translate_dict(cls, val):
        pass

    @classmethod
    def translate_list(cls, val):
        pass

    @classmethod
    def comment(cls, cmt_str):
        pass

    @classmethod
    def codify(cls, parameters, comment='Parameters'):
        pass

class CSharpTranslator(Translator):

    @classmethod
    def translate_none(cls, val):
        pass

    @classmethod
    def translate_bool(cls, val):
        pass

    @classmethod
    def translate_int(cls, val):
        pass

    @classmethod
    def translate_dict(cls, val):
        """Translate dicts to nontyped dictionary"""
        pass

    @classmethod
    def translate_list(cls, val):
        """Translate list to array"""
        pass

    @classmethod
    def comment(cls, cmt_str):
        pass

    @classmethod
    def assign(cls, name, str_val):
        pass

class FSharpTranslator(Translator):

    @classmethod
    def translate_none(cls, val):
        pass

    @classmethod
    def translate_bool(cls, val):
        pass

    @classmethod
    def translate_int(cls, val):
        pass

    @classmethod
    def translate_dict(cls, val):
        pass

    @classmethod
    def translate_list(cls, val):
        pass

    @classmethod
    def comment(cls, cmt_str):
        pass

    @classmethod
    def assign(cls, name, str_val):
        pass

class PowershellTranslator(Translator):

    @classmethod
    def translate_escaped_str(cls, str_val):
        """Translate a string to an escaped Matlab string"""
        pass

    @classmethod
    def translate_float(cls, val):
        pass

    @classmethod
    def translate_none(cls, val):
        pass

    @classmethod
    def translate_bool(cls, val):
        pass

    @classmethod
    def translate_dict(cls, val):
        pass

    @classmethod
    def translate_list(cls, val):
        pass

    @classmethod
    def comment(cls, cmt_str):
        pass

    @classmethod
    def assign(cls, name, str_val):
        pass

class BashTranslator(Translator):

    @classmethod
    def translate_none(cls, val):
        pass

    @classmethod
    def translate_bool(cls, val):
        pass

    @classmethod
    def translate_escaped_str(cls, str_val):
        pass

    @classmethod
    def translate_list(cls, val):
        pass

    @classmethod
    def comment(cls, cmt_str):
        pass

    @classmethod
    def assign(cls, name, str_val):
        pass
papermill_translators = PapermillTranslators()
papermill_translators.register('python', PythonTranslator)
papermill_translators.register('R', RTranslator)
papermill_translators.register('scala', ScalaTranslator)
papermill_translators.register('julia', JuliaTranslator)
papermill_translators.register('matlab', MatlabTranslator)
papermill_translators.register('.net-csharp', CSharpTranslator)
papermill_translators.register('.net-fsharp', FSharpTranslator)
papermill_translators.register('.net-powershell', PowershellTranslator)
papermill_translators.register('pysparkkernel', PythonTranslator)
papermill_translators.register('sparkkernel', ScalaTranslator)
papermill_translators.register('sparkrkernel', RTranslator)
papermill_translators.register('bash', BashTranslator)

def translate_parameters(kernel_name, language, parameters, comment='Parameters'):
    pass
