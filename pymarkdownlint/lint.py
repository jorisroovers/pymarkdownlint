from __future__ import print_function
from pymarkdownlint import rules


class MarkdownLinter(object):
    def __init__(self):
        self.rules = [rules.MaxLineLengthRule(), rules.TrailingWhiteSpace(), rules.HardTab()]

    def lint_files(self, files):
        """
        Lints a list of files.
        :param files: list of files to lint
        :return: a list of violations found in the files
        """
        all_violations = []
        for filename in files:
            with open(filename, 'r') as f:
                content = f.read()
                violations = self.lint(content)
                all_violations.extend(violations)
                for e in violations:
                    print("{0}:{1}: {2} {3}".format(filename, e.line_nr, e.rule_id, e.message))
        return len(all_violations)

    def lint(self, markdown_string):
        all_violations = []
        lines = markdown_string.split("\n")
        for rule in self.rules:
            if isinstance(rule, rules.LineRule):
                line_nr = 1
                for line in lines:
                    violation = rule.validate(line)
                    if violation:
                        violation.line_nr = line_nr
                        all_violations.append(violation)
                    line_nr += 1
        return all_violations
