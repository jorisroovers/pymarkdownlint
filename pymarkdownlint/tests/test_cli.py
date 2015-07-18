from pymarkdownlint.tests.base import BaseTestCase

from pymarkdownlint import cli


class CLITests(BaseTestCase):
    def test_cli(self):
        self.assertEqual(cli.get_foo(), "foo")
