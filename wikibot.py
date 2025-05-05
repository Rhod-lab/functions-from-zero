import click
import wikipedia
@click.command()
@click.option('--name', prompt='wikipedia page to scrape',
                help='web page we want to scrape')

    click.echo(click.style(f"{result}:", fg="blue"))
if __name__== '__main__':
    scrape()