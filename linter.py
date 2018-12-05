# Copyright 2018 Jordon Bedwell. All rights reserved.
# Use of this source code is governed by the MIT license
# that can be found in the LICENSE file.

from SublimeLinter.lint import util, Linter, WARNING
from os import path

class GoLint(Linter):
    tempfile_suffix = "-"
    default_type = WARNING
    defaults = { 'selector': 'source.go' }
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?(:(?:(?P<warning>warning)|(?P<error>error)))?:\s*(?P<message>.*)'
    error_stream = util.STREAM_STDOUT

    def cmd(self):
      r = self.relative_path
      e = self.which("gometalinter")
      if e is not None and r is not "":
        return (e, "--include", r, "${args}", "${folder}",)
      return None

    @property
    def relative_path(self):
      f = self.filename
      d = self.get_working_dir(self.settings)
      if d is not "" and f is not "":
        return path.relpath(f, d)
      return f

    def finalize_cmd(self, cmd, context, at_value='', auto_append=False):
      return super().finalize_cmd(cmd, context,
        at_value, auto_append=False)

    def get_working_dir(self, settings):
      f = self.filename
      s = self.settings
      if f is "":
        return super().get_working_dir(s)
      return path.dirname(f)
