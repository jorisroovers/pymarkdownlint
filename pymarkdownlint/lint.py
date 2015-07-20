from __future__ import print_function
from pymarkdownlint.rules import MaxLineLengthRule, TrailingWhiteSpace, RuleError


class MarkdownLinter(object):
    def __init__(self):
        self.rules = [MaxLineLengthRule(), TrailingWhiteSpace()]

    def lint_files(self, files):
        all_errors = []
        for filename in files:
            with open(filename, 'r') as f:
                content = f.read()
                errors = self.lint(content)
                all_errors.extend(errors)
                for e in errors:
                    print("{0}:{1}: {2} {3}".format(filename, e.line_nr, e.rule_id, e.message))
        return len(all_errors)

    def lint(self, markdown_string):
        all_errors = []
        for rule in self.rules:
            all_errors.extend(rule.validate(markdown_string))
        return all_errors
