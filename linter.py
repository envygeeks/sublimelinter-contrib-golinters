from SublimeLinter.lint import util, Linter, WARNING


class GoLint(Linter):
    default_type = WARNING
    error_stream = util.STREAM_STDOUT
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?(:(?:(?P<warning>warning)|(?P<error>error)))?:\s*(?P<message>.*)'
    cmd = 'gometalinter --fast --concurrency=12 ${file}'
    defaults = {
        'selector': 'source.go'
    }
