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
      f = self.filename
      e = self.which("gometalinter")
      a = tuple()

      if e is not None:
        if f is not "":
          f = path.relpath(f, self.get_working_dir(self.settings))
          i = "--include='^{}'".format(f)
          a += (i,)
        else:
          f = "."

        return a + ("${args}", f, "${file}",)
      return None

    def finalize_cmd(self, cmd, context, at_value='', auto_append=False):
      f = self.filename
      c = super().finalize_cmd(cmd, context, at_value, auto_append)
      if f is not "": c[:] = [a for a in c if a != f]
      return c

    def get_working_dir(self, settings):
      f = self.filename
      if f is not "": f = path.dirname(self.filename)
      return f
