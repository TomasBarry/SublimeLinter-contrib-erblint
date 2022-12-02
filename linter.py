from SublimeLinter.lint import util, Linter


class ERBLint(Linter):
    """A linter for Embedded Ruby files (.erb)

    This class extends SublimeLinter.lint.Linter. It defines the most basic set
    of configs for running the 'out of the box' version of `erblint`

    An example output of `erblint ~/path/to/file.erb is:

    ```
    .erb-lint.yml not found: using default config
    Linting 1 files with 12 linters...

    ...

    Tag `input` is self-closing, it must end with `/>`.
    In file: path/to/file.html.erb:123

    ...

    12 error(s) were found in ERB files
    ```

    The regex defined below matches the error output from `erblint`. In order to
    ignore the extra warning (when not passing a config file to `erblint`) we
    set `error_stream` to `util.STREAM_STDOUT`.
    """
    cmd = 'erblint ${args} ${temp_file}'
    regex = (
        r'^(?P<message>.*)\n'
        r'In file: .*:(?P<line>[0-9]+)'
    )
    multiline = True
    tempfile_suffix = 'erb'
    error_stream = util.STREAM_STDOUT
    defaults = {
        'selector': 'text.html.ruby, text.html.rails'
    }
