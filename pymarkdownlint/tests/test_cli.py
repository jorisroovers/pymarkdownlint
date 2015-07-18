from pymarkdownlint.tests.base import BaseTestCase

from pymarkdownlint import cli

from click.testing import CliRunner


class CLITests(BaseTestCase):
    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli.cli)
        self.assertEqual(result.output, "foo\n")
