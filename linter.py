# Copyright 2018 Jordon Bedwell. All rights reserved.
# Use of this source code is governed by the MIT license
# that can be found in the LICENSE file.

from os import path
from SublimeLinter.lint import util, Linter, WARNING
import re

class GoLint(Linter):
    defaults = { "selector": "source.go" }
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?(:(?:(?P<warning>warning)|(?P<error>error)))?:\s*(?P<message>.*)'
    tempfile_suffix = "-"

    @property
    def relative_path(self):
      f = self.filename
      d = self.get_working_dir(self.settings)
      if d is not "" and f is not "":
        return path.relpath(f, d)
      return f

    def cmd(self):
      i, r = tuple(), self.relative_path
      if r is not "": i = ("--include", "^{}".format(r),)
      return ("gometalinter",) + i + \
        ("${args}", ".",)

    def finalize_cmd(self, cmd, context, at_value='', auto_append=False):
      return super().finalize_cmd(cmd, context,
        at_value, auto_append=False)

    def get_working_dir(self, settings):
      f, s = self.filename, self.settings
      if f is "":
        return super().get_working_dir(s)
      return path.dirname(f)
