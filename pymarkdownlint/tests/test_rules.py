from pymarkdownlint.tests.base import BaseTestCase
from pymarkdownlint.rules import MaxLineLengthRule, TrailingWhiteSpace, RuleError


class RuleTests(BaseTestCase):
    def test_max_line_length(self):
        rule = MaxLineLengthRule()
        line_nr = 1

        # assert no error
        rule.validate_line("a" * 80, line_nr)

        # assert error on line length > 81
        with self.assertRaises(RuleError):
            rule.validate_line("a" * 81, line_nr)

        # set line length to 120, and assert no raise on length 81
        rule = MaxLineLengthRule({'line-length': 120})
        rule.validate_line("a" * 81, line_nr)

        # assert raise on 121
        with self.assertRaises(RuleError):
            rule.validate_line("a" * 121, line_nr)

    def test_trailing_whitespace(self):
        rule = TrailingWhiteSpace()
        line_nr = 1

        # assert no error
        rule.validate_line("a", line_nr)

        # trailing space
        expected_error = "Line has trailing whitespace"
        with self.assertRaisesRegexp(RuleError, expected_error):
            rule.validate_line("a ", line_nr)

        # trailing tab
        with self.assertRaisesRegexp(RuleError, expected_error):
            rule.validate_line("a\t", line_nr)
