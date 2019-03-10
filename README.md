SublimeLinter-contrib-erblint
================================

[![Build Status](https://travis-ci.org/TomasBarry/SublimeLinter-contrib-erblint.svg?branch=master)](https://travis-ci.org/TomasBarry/SublimeLinter-contrib-erblint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [erblint](https://github.com/justinthec/erb-lint). It will be used with files that have the “erb” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `erblint` is installed on your system.

1. Install [Ruby](http://ruby-lang.org).

1. Install `erblint` by typing the following in a terminal:
   ```
   [sudo] gem install erblint
   ```

1. If you are using `rvm` or `rbenv`, ensure that they are loaded in your shell’s correct startup file. See [here](http://sublimelinter.com/en/latest/troubleshooting.html#adjusting-shell-startup-files) for more information.

In order for `erblint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
