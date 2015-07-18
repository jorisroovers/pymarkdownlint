# pymarkdownlint [![Build Status](https://travis-ci.org/jorisroovers/pymarkdownlint.svg?branch=master)](https://travis-ci.org/jorisroovers/pymarkdownlint)
Markdown linter written in python. Inspired by mivok/markdownlint.

Get started by running:
```bash
markdownlint examples/
```

If you only want to list the files that will be checked: 
```bash
markdownlint --list-files examples/
```

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
- Better output handling