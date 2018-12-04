from SublimeLinter.lint import util, Linter, WARNING
from os import path


class GoLint(Linter):
    tempfile_suffix = "-"
    default_type = WARNING
    defaults = { 'selector': 'source.go' }
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?(:(?:(?P<warning>warning)|(?P<error>error)))?:\s*(?P<message>.*)'
    error_stream = util.STREAM_STDOUT

    def cmd(self):
      e = self.which("gometalinter")
      f = path.basename(self.filename)
      return (e, "${args}", f, "${file}") if e != None and f != ""
      return None

    def finalize_cmd(self, cmd, context, at_value='', auto_append=False):
      f = self.filename
      c = super().finalize_cmd(cmd, context, at_value, auto_append)
      c[:] = [a for a in c if a != f] if f != ""
      return c
