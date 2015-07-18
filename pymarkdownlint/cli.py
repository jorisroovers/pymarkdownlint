from pymarkdownlint.filefinder import MarkdownFileFinder
import click


def echo_files(files):
    for f in files:
        click.echo(f)
    exit(0)


@click.command()
@click.option('--list-files', is_flag=True)
@click.argument('path', type=click.Path(exists=True))
def cli(list_files, path):
    """ Markdown lint tool, checks your markdown for styling issues """
    files = MarkdownFileFinder.find_files(path)
    if list_files:
        echo_files(files)
    click.echo("foo")


if __name__ == "__main__":
    cli()
