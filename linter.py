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
      e = self.base_cmd()
      if e is not None:
        if f is not "":
          d = self.get_working_dir(self.settings)
          f = path.relpath(f, d)
          # i = "--include='^{}'".format(f)
          # e += (i,)
        else:
          f = "."

        return e + ("${args}", f, "${file}",)
      return None

    def base_cmd(self):
      e = self.which("gometalinter")
      if e is not None: return (e, "--aggregate",)
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
