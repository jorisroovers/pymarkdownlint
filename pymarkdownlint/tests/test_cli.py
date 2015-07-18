from pymarkdownlint.tests.base import BaseTestCase
from pymarkdownlint import cli

from click.testing import CliRunner


class CLITests(BaseTestCase):
    def setUp(self):
        self.cli = CliRunner()

    def assert_output_line(self, output, index, sample_filename, error_line, expected_error):
        expected_output = "{0}:{1}: {2}".format(self.get_sample_path(sample_filename), error_line, expected_error)
        self.assertEqual(output.split("\n")[index], expected_output)

    def test_no_errors(self):
        result = self.cli.invoke(cli.cli, [self.get_sample_path("good.md")])
        self.assertEqual(result.output, "")

    def test_errors(self):
        result = self.cli.invoke(cli.cli, [self.get_sample_path("sample1.md")])
        self.assert_output_line(result.output, 0, "sample1.md", 3, "Line exceeds max length (119>80)")

    def test_cli_list_files(self):
        result = self.cli.invoke(cli.cli, ["--list-files", self.get_sample_path()])
        expected_string = ""
        expected_files = ["good.md", "sample1.md", "sample2.md"]
        for f in expected_files:
            expected_string += self.get_sample_path(f) + "\n"
        self.assertEqual(result.output, expected_string)
