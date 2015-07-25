from pymarkdownlint.tests.base import BaseTestCase
from pymarkdownlint.rules import MaxLineLengthRule, TrailingWhiteSpace, RuleViolation


class RuleTests(BaseTestCase):
    def test_max_line_length(self):
        rule = MaxLineLengthRule()

        # assert no error
        violation = rule.validate("a" * 80)
        self.assertIsNone(violation)

        # assert error on line length > 81
        expected_violation = RuleViolation("R1", "Line exceeds max length (81>80)")
        violation = rule.validate("a" * 81)
        self.assertEqual(violation, expected_violation)

        # set line length to 120, and check no violation on length 81
        rule = MaxLineLengthRule({'line-length': 120})
        violation = rule.validate("a" * 81)
        self.assertIsNone(violation)

        # assert raise on 121
        expected_violation = RuleViolation("R1", "Line exceeds max length (121>120)")
        violation = rule.validate("a" * 121)
        self.assertEqual(violation, expected_violation)

    def test_trailing_whitespace(self):
        rule = TrailingWhiteSpace()

        # assert no error
        violation = rule.validate("a")
        self.assertIsNone(violation)

        # trailing space
        expected_violation = RuleViolation("R2", "Line has trailing whitespace")
        violation = rule.validate("a ")
        self.assertEqual(violation, expected_violation)

        # trailing tab
        violation = rule.validate("a\t")
        self.assertEqual(violation, expected_violation)
