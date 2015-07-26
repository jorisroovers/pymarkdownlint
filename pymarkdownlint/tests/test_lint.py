from pymarkdownlint.tests.base import BaseTestCase

from pymarkdownlint.lint import MarkdownLinter
from pymarkdownlint.rules import RuleViolation
from pymarkdownlint.config import LintConfig


class RuleOptionTests(BaseTestCase):
    def test_lint(self):
        linter = MarkdownLinter(LintConfig())
        sample = self.get_sample_path("sample1.md")
        with open(sample) as f:
            errors = linter.lint(f.read())
            expected_errors = [RuleViolation("R1", "Line exceeds max length (119>80)", 3),
                               RuleViolation("R2", "Line has trailing whitespace", 4),
                               RuleViolation("R2", "Line has trailing whitespace", 5),
                               RuleViolation("R3", "Line contains hard tab characters (\\t)", 5)]
            self.assertListEqual(errors, expected_errors)
