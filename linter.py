from SublimeLinter.lint import Linter
import os
import re
import sublime
import sublime_plugin
import tempfile

OUTPUT_RE = re.compile(r'(?P<filename>^.+?):?\(?(?P<line>\d+)\)?:((?P<col>\d+):)?'
             r'\s*\w*\s*((?P<error>error)|(?P<warning>warning)):'
             r'\s*(?P<message>.+)')


class Nvcc(Linter):
    name = "nvcc"
    cmd = "nvcc"
    regex = OUTPUT_RE
    multiline = True
    on_stderr = None

    defaults = {
        "selector": "source.cu",
    }


class SublimeLinterGccRunTests(sublime_plugin.WindowCommand):
    """
    To do unittests, run the following command in ST's console:
    window.run_command('sublime_linter_gcc_run_tests')
    """

    def run(self):
        from .tests.regex_tests import run_tests

        run_tests(Nvcc.regex)
