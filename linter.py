from SublimeLinter.lint import util, Linter, WARNING
from os import path


class GoLint(Linter):
    tempfile_suffix = "-"
    default_type = WARNING
    defaults = { 'selector': 'source.go' }
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?(:(?:(?P<warning>warning)|(?P<error>error)))?:\s*(?P<message>.*)'
    error_stream = util.STREAM_STDOUT

    def cmd(self):
      print("golinters: {}".format(self.settings))

      f = self.filename
      e = self.which("gometalinter")
      t = ("/usr/bin/env", "GO111MODULE=auto", e)
      if f != "": f = path.relpath(f, self.get_working_dir(self.settings))
      if e is not None and f is not "": return t + ("${args}", f, "${file}")
      return None

    def finalize_cmd(self, cmd, context, at_value='', auto_append=False):
      f = self.filename
      c = super().finalize_cmd(cmd, context, at_value, auto_append)
      if f is not "": c[:] = [a for a in c if a != f]
      return c
