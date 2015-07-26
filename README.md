# pymarkdownlint

[![Build Status](https://travis-ci.org/jorisroovers/pymarkdownlint.svg?branch=master)]
(https://travis-ci.org/jorisroovers/pymarkdownlint)
[![PyPi Package](https://img.shields.io/pypi/v/pymarkdownlint.png)]
(https://pypi.python.org/pypi/pymarkdownlint)

Markdown linter written in python. Inspired by [mivok/markdownlint](https://github.com/mivok/markdownlint).

**NOTE: pymarkdownlint is still under active development and missing many core features**

Get started by running:
```bash
markdownlint examples/             # lint all files in a directory
markdownlint examples/example1.md  # lint a single file
markdownlint examples/example1.md  # lint a single file
```
NOTE: The returned exit code equals the number of errors found.

Other commands and variations:

```bash
Usage: markdownlint [OPTIONS] PATH

Markdown lint tool, checks your markdown for styling issues

Options:
  --config PATH  Config file location (default: .markdownlint).
  --list-files   List markdown files in given path and exit.
  --ignore TEXT  Ignore rules (comma-separated by id or name).
  --version      Show the version and exit.
  --help         Show this message and exit.
```

You can modify pymarkdownlint's behavior by specifying a config file like so: 
```bash
markdownlint --config myconfigfile 
```
By default, markdownlint will look for an **optional** ```.markdownlint``` file for configuration.

## Config file ##

```
[general]
# rules can be ignored by name or by id
ignore=max-line-length, R3
```

## Supported Rules ##

ID    | Name                | Description
------|---------------------|----------------------------------------------------
R1    | max-line-length     | Line length must be &lt; 80 chars.
R2    | trailing-whitespace | Line cannot have trailing whitespace (space or tab)
R3    | hard-tabs           | Line contains hard tab characters (\t)


## Development ##

To run tests:
```bash
./run_tests.sh                       # run unit tests and print test coverage
./run_tests.sh --no-coverage         # run unit tests without test coverage
./run_tests.sh --pep8                # pep8 checks
./run_tests.sh --stats               # print some code stats
```

There is a Vagrantfile in this repository that can be used for development.
```bash
vagrant up
vagrant ssh
```

## Wishlist ##
- More rules!
- Better output handling with verbosity levels
- Ignore/exclude files CLI options
- Rule specific configuration in config files
- Auto doc generation based on rules
