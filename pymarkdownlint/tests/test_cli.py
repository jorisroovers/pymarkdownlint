from pymarkdownlint.tests.base import BaseTestCase
from pymarkdownlint import cli

from click.testing import CliRunner


class CLITests(BaseTestCase):
    def setUp(self):
        self.cli = CliRunner()

    def test_cli(self):
        result = self.cli.invoke(cli.cli, [self.get_sample_path()])
        self.assertEqual(result.output, "foo\n")

    def test_cli_list_files(self):
        result = self.cli.invoke(cli.cli, ["--list-files", self.get_sample_path()])
        sample1 = self.get_sample_path("sample1.md")
        sample2 = self.get_sample_path("sample2.md")
        self.assertEqual(result.output, sample1 + "\n" + sample2 + "\n")
