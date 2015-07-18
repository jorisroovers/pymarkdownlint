import click


@click.command()
def cli():
    """ Markdown lint tool, checks your markdown for styling issues """
    click.echo("foo")


if __name__ == "__main__":
    cli()
