from pymarkdownlint.tests.base import BaseTestCase

from pymarkdownlint.lint import MarkdownLinter
from pymarkdownlint.rules import RuleError


class RuleOptionTests(BaseTestCase):
    def test_lint(self):
        linter = MarkdownLinter()
        sample = self.get_sample_path("sample1.md")
        with open(sample) as f:
            errors = linter.lint(f.read())
            self.assertListEqual(errors, [RuleError(3, 'Line exceeds max length (119>80)')])
