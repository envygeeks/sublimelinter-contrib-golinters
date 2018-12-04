from SublimeLinter.lint import util, Linter, WARNING
from os import path


class GoLint(Linter):
    tempfile_suffix = "-"
    default_type = WARNING
    defaults = { 'selector': 'source.go' }
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?(:(?:(?P<warning>warning)|(?P<error>error)))?:\s*(?P<message>.*)'
    args = ("--fast", "${args}", "${file}")
    error_stream = util.STREAM_STDOUT

    def cmd(self):
      """Gives back the command with a relative path."""
      f, e = path.basename(self.filename), self.which("gometalinter")
      if e is not None and f is not "":
        # We'll still get a dep and have to strip it out 🤷‍♂️
        return (e,) + self.args + ("${args}", f, "${file}")
      return None

    def finalize_cmd(self, cmd, context, at_value='', auto_append=False):
      c = super().finalize_cmd(cmd, context, at_value, auto_append)
      print("golinters: finalize_cmd original got {}".format(c))
      f = self.filename
      if f is not "":
        i = c.index(f)
        print("golinters: index at {}".format(i))
        del c[i]

      print("golinters: returning {}".format(c))
      return c
