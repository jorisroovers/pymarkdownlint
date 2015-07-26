import pymarkdownlint
from pymarkdownlint.filefinder import MarkdownFileFinder
from pymarkdownlint.lint import MarkdownLinter
from pymarkdownlint.config import LintConfig
import os
import click

DEFAULT_CONFIG_FILE = ".markdownlint"


def echo_files(files):
    for f in files:
        click.echo(f)
    exit(0)


def get_lint_config(config_path=None):
    """ Tries loading the config from the given path. If no path is specified, the default config path
    is tried, and if that is not specified, we the default config is returned. """
    # config path specified
    if config_path:
        config = LintConfig.load_from_file(config_path)
        click.echo("Using config from {0}".format(config_path))
    # default config path
    elif os.path.exists(DEFAULT_CONFIG_FILE):
        config = LintConfig.load_from_file(DEFAULT_CONFIG_FILE)
        click.echo("Using config from {0}".format(DEFAULT_CONFIG_FILE))
    # no config file
    else:
        config = LintConfig()

    return config


@click.command()
@click.option('--config', type=click.Path(exists=True),
              help="Config file location (default: {0}).".format(DEFAULT_CONFIG_FILE))
@click.option('--list-files', is_flag=True, help="List markdown files in given path and exit.")
@click.option('--ignore', default="", help="Ignore rules (comma-separated by id or name).")
@click.argument('path', type=click.Path(exists=True))
@click.version_option(version=pymarkdownlint.__version__)
def cli(list_files, config, ignore, path):
    """ Markdown lint tool, checks your markdown for styling issues """
    files = MarkdownFileFinder.find_files(path)
    if list_files:
        echo_files(files)

    lint_config = get_lint_config(config)
    lint_config.apply_on_csv_string(ignore, lint_config.disable_rule)

    linter = MarkdownLinter(lint_config)
    error_count = linter.lint_files(files)
    exit(error_count)


if __name__ == "__main__":
    cli()
