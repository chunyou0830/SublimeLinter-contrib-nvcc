#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by BlahGeek
# Copyright (c) 2017
#
# License: MIT
#

"""This module exports the Nvcc plugin class."""

# import os
# import shlex
# import string
# import tempfile
# import sublime
import sublime_plugin
from SublimeLinter.lint import Linter, util

OUTPUT_RE = (r'(?P<filename>^.+?):?\(?(?P<line>\d+)\)?:((?P<col>\d+):)?'
             r'\s*\w*\s*((?P<error>error)|(?P<warning>warning)):'
             r'\s*(?P<message>.+)')


class Nvcc(Linter):
    """Provides an interface to nvcc."""

    name = 'nvcc'

    regex = OUTPUT_RE

    tempfile_suffix = 'cu'
    error_stream = util.STREAM_STDERR

    defaults = {
        'selector': 'source.cu'
        # 'include_dirs': [],
        # 'extra_flags': ''
    }

    cmd = 'nvcc'


class SublimeLinterGccRunTests(sublime_plugin.WindowCommand):
    """
    To do unittests, run the following command in ST's console:
    window.run_command('sublime_linter_gcc_run_tests')
    """

    def run(self):
        from .tests.regex_tests import run_tests

        run_tests(Nvcc.regex)
