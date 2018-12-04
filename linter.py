from SublimeLinter.lint import util, Linter, WARNING
from os import path


class GoLint(Linter):
    tempfile_suffix = "-"
    default_type = WARNING
    defaults = { 'selector': 'source.go' }
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?(:(?:(?P<warning>warning)|(?P<error>error)))?:\s*(?P<message>.*)'
    error_stream = util.STREAM_STDOUT
    default_args = ("--fast")

    def cmd(self):
      """Gives back the command with a relative path."""
      f, e = path.basename(self.filename), self.which("gometalinter")
      if e is not None and f is not "":
        return (e,) + self.default_args + (
          "${args}", f, "${file}")
      return None

    def finalize_cmd(self, cmd, context, at_value='', auto_append=False):
      c, f = super().finalize_cmd(cmd, context, at_value, auto_append), self.filename
      if f is not "":
        del c[c.index(f)]
      return c
