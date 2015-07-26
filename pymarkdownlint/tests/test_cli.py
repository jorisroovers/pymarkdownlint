from pymarkdownlint.tests.base import BaseTestCase
from pymarkdownlint import cli
from pymarkdownlint import __version__

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
        self.assertEqual(result.exit_code, 0)

    def test_version(self):
        result = self.cli.invoke(cli.cli, ["--version"])
        self.assertEqual(result.output.split("\n")[0], "cli, version {0}".format(__version__))

    def test_config_file(self):
        args = ["--config", self.get_sample_path("markdownlint"), self.get_sample_path("sample1.md")]
        result = self.cli.invoke(cli.cli, args)
        expected_string = "Using config from {0}".format(self.get_sample_path("markdownlint"))
        self.assertEqual(result.output.split("\n")[0], expected_string)
        self.assert_output_line(result.output, 1, "sample1.md", 4, "R2 Line has trailing whitespace")
        self.assert_output_line(result.output, 2, "sample1.md", 5, "R2 Line has trailing whitespace")
        self.assertEqual(result.exit_code, 2)

    def test_config_file_negative(self):
        args = ["--config", self.get_sample_path("foo"), self.get_sample_path("sample1.md")]
        result = self.cli.invoke(cli.cli, args)
        expected_string = "Error: Invalid value for \"--config\": Path \"{0}\" does not exist.".format(
            self.get_sample_path("foo"))
        self.assertEqual(result.output.split("\n")[2], expected_string)

    def test_violations(self):
        result = self.cli.invoke(cli.cli, [self.get_sample_path("sample1.md")])
        self.assert_output_line(result.output, 0, "sample1.md", 3, "R1 Line exceeds max length (119>80)")
        self.assert_output_line(result.output, 1, "sample1.md", 4, "R2 Line has trailing whitespace")
        self.assert_output_line(result.output, 2, "sample1.md", 5, "R2 Line has trailing whitespace")
        self.assert_output_line(result.output, 3, "sample1.md", 5, "R3 Line contains hard tab characters (\\t)")
        self.assertEqual(result.exit_code, 4)

    def test_violations_with_ignored_rules(self):
        args = ["--ignore", "trailing-whitespace,R3", self.get_sample_path("sample1.md")]
        result = self.cli.invoke(cli.cli, args)
        self.assert_output_line(result.output, 0, "sample1.md", 3, "R1 Line exceeds max length (119>80)")
        self.assertEqual(result.exit_code, 1)

    def test_cli_list_files(self):
        result = self.cli.invoke(cli.cli, ["--list-files", self.get_sample_path()])
        expected_string = ""
        expected_files = ["good.md", "sample1.md", "sample2.md"]
        for f in expected_files:
            expected_string += self.get_sample_path(f) + "\n"
        self.assertEqual(result.output, expected_string)
        self.assertEqual(result.exit_code, 0)
