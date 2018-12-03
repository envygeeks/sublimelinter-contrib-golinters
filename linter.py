from SublimeLinter.lint import Linter


class GoLint(Linter):
    multiline = False
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?:(?:(?P<warning>warning)|(?P<error>error)):\s*(?P<message>.*)'
    cmd = 'gometalinter'

    args = (
      "--fast",
      "--concurrency=12",
      "--disable-all",
      "--vendor",
      "--tests",

      "--enable=gosec",
      "--enable=golint",
      "--enable=errcheck",
      "--enable=ineffassign",
      "--enable=vetshadow",
      "--enable=goconst",
      "--enable=gocyclo",
      "--enable=deadcode",
      "--enable=safesql"
    )

    defaults = {
        'selector': 'source.go'
    }
