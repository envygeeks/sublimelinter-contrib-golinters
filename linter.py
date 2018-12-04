from SublimeLinter.lint import util, Linter, WARNING
from os import path


class GoLint(Linter):
    tempfile_suffix = "-"
    default_type = WARNING
    defaults = { 'selector': 'source.go' }
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?(:(?:(?P<warning>warning)|(?P<error>error)))?:\s*(?P<message>.*)'
    args = ("--fast", "--concurrency=12", "${args}")
    error_stream = util.STREAM_STDOUT

    def cmd(self):
      """Gives back the command with a relative path."""
      f, e = path.basename(self.filename), self.which("gometalinter")
      if e is not None and f is not "":
        return (e,) + self.args
      return None

    def get_cmd(self):
      args = super().get_cmd()
      print('golinters: {}'.format(args))
      if args[-1] == self.filename:
        del args[-1]
      return args
