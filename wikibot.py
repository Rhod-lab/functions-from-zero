import click
from mylib.bot import scrape

@click.command()
@click.option('--name',
              help='web page we want to scrape')
@click.option('--length',
              help='length of the output from wipedia')

def cli(name, length):
    result = scrape(name, length=length)
    click.echo(click.style(f"{result}:", bg="green", fg="white"))

if __name__== '__main__':
    cli()