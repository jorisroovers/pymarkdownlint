from __future__ import print_function
from pymarkdownlint.rules import MaxLineLengthRule, RuleError


class MarkdownLinter(object):
    def __init__(self):
        self.rules = [MaxLineLengthRule()]

    def lint_files(self, files):
        for filename in files:
            with open(filename, 'r') as f:
                content = f.read()
                errors = self.lint(content)
                for e in errors:
                    print("{0}:{1}: {2}".format(filename, e.line_nr, e.message))

    def lint(self, markdown_string):
        errors = []
        for rule in self.rules:
            try:
                rule.validate(markdown_string)
            except RuleError as e:
                errors.append(e)
        return errors
