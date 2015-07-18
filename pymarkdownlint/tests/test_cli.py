from pymarkdownlint.tests.base import BaseTestCase

from pymarkdownlint import cli

from click.testing import CliRunner


class CLITests(BaseTestCase):
    def setUp(self):
        self.cli = CliRunner()

    def test_cli(self):
        result = self.cli.invoke(cli.cli)
        self.assertEqual(result.output, "foo\n")
