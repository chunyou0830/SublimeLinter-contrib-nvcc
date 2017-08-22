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

import os
import shlex
import string
import tempfile
import sublime
from SublimeLinter.lint import Linter, util


def get_project_folder():
    """Get project folder of current file or current file's dir."""
    proj_file = sublime.active_window().project_file_name()
    if proj_file:
        return os.path.dirname(proj_file)
    # Use current file's folder when no project file is opened.
    proj_file = sublime.active_window().active_view().file_name()
    if proj_file:
        return os.path.dirname(proj_file)
    return '.'


def apply_template(s):
    """Substitude '${project_folder}' in string."""
    mapping = {
        "project_folder": get_project_folder()
    }
    templ = string.Template(s)
    return templ.safe_substitute(mapping)


class Nvcc(Linter):
    """Provides an interface to nvcc."""

    syntax = ('cuda-c++', 'cuda-c', 'cuda')
    executable = 'nvcc'

    regex = (r'(?P<filename>^.+?):?\(?(?P<line>\d+)\)?:((?P<col>\d+):)?'
             r'\s*\w*\s*((?P<error>error)|(?P<warning>warning)):'
             r'\s*(?P<message>.+)')

    tempfile_suffix = 'cu'
    error_stream = util.STREAM_STDERR

    defaults = {
        'include_dirs': [],
        'extra_flags': ''
    }

    cmd = 'nvcc'

    def cmd(self):
        """
        Return the command line to execute.

        We override this method, so we can add extra flags and include paths
        based on the 'include_dirs' and 'extra_flags' settings.
        """
        result = 'nvcc -cuda '

        settings = self.get_view_settings()
        result += apply_template(settings.get('extra_flags', ''))

        include_dirs = settings.get('include_dirs', [])
        result += apply_template(' '.join([' -I ' + shlex.quote(include)
                                          for include in include_dirs]))

        tempdir = tempfile.gettempdir()
        tempfilename = os.path.join(tempdir, 'nvcc-linter-output.ii')
        result += ' -o {} '.format(tempfilename)

        return result + ' @'

    def split_match(self, match):
        """Filter matches that matches current filename."""
        m = list(super().split_match(match))
        filename = m[0].group('filename') if m[0] else ''
        if filename and \
           os.path.basename(filename) != os.path.basename(self.filename):
            m[0] = None
        return m
