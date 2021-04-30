from __future__ import print_function
from pymarkdownlint import rules


class MarkdownLinter(object):
    def __init__(self, config):
        self.config = config

    @property
    def line_rules(self):
        return [rule for rule in self.config.rules if isinstance(rule, rules.LineRule)]
    @property
    def file_rules(self):
        return [rule for rule in self.config.rules if isinstance(rule, rules.FileRule)]

    def _apply_file_rules(self, markdown_string):
        file_violations = []
        ignoring = False
        if ignoring:
            if markdown_string.strip() == '<!-- markdownlint:enable -->':
                ignoring = False
        else:
            if markdown_string.strip() == '<!-- markdownlint:disable -->':
                ignoring = True

            for rule in self.file_rules:
                violation = rule.validate(markdown_string)
                if violation:
                    violation.rule_id = rule.id
                    file_violations.append(violation)
        return file_violations

    def _apply_line_rules(self, markdown_string):
        """ Iterates over the lines in a given markdown string and applies all the enabled line rules to each line """
        line_violations = []
        lines = markdown_string.split("\n")
        line_nr = 1
        ignoring = False
        for line in lines:
            if ignoring:
                if line.strip() == '<!-- markdownlint:enable -->':
                    ignoring = False
            else:
                if line.strip() == '<!-- markdownlint:disable -->':
                    ignoring = True
                    continue

                for rule in self.line_rules:
                    violation = rule.validate(line)
                    if violation:
                        violation.line_nr = line_nr
                        line_violations.append(violation)
            line_nr += 1
        return line_violations

    def lint(self, markdown_string):
        file_rules = self._apply_file_rules(markdown_string)
        line_rules = self._apply_line_rules(markdown_string)
        return file_rules + line_rules

    def lint_files(self, files):
        """ Lints a list of files.
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
