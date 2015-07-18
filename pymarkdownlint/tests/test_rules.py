from pymarkdownlint.tests.base import BaseTestCase
from pymarkdownlint.rules import MaxLineLengthRule, RuleError


class RuleTests(BaseTestCase):

    def test_max_line_length(self):
        rule = MaxLineLengthRule()

        # assert no error
        rule.validate("a" * 80)

        # assert error on line length > 81
        with self.assertRaises(RuleError):
            rule.validate("a" * 81)

        # set line length to 120, and assert no raise on length 81
        rule = MaxLineLengthRule({'line-length': 120})
        rule.validate("a" * 81)

        # assert raise on 121
        with self.assertRaises(RuleError):
            rule.validate("a" * 121)
