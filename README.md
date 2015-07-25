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

If you only want to list the files that will be checked: 
```bash
markdownlint --list-files examples/
markdownlint --help                # show more commands
```

## Supported Rules ##

ID    | Name                | Description
------|---------------------|----------------------------------------------------
R1    | Max line length     | Line length must be &lt; 80 chars.
R2    | Trailing whitespace | Line cannot have trailing whitespace (space or tab)


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
- Refactor rule engine, line rules vs. file rules
- More rules!
- Better output handling with verbosity levels
- Ignore files CLI options
- Disable rules CLI options
- .markdownlint config support
- Auto doc generation based on rules
