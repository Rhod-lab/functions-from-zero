import wikipedia

# import click

# @click.command()
# @click.option('--name', prompt='wikipedia page to scrape',
#                help='web page we want to scrape')

def scrape (name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=length)
    return result
print(scrape("wikipedia"))

#   click.echo(click.style(f"{result}:", fg="blue"))

#if __name__== '__main__':
#    scrape()