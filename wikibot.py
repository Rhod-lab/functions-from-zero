# import click
import wikipedia
def scrape (name="Microsoft", lenth=1):
    result = wikipedia.summary(name, sentences=lenth)
    return result
print(scrape("Facebook"))

# @click.command()
# @click.option('--name', prompt='wikipedia page to scrape',
#                help='web page we want to scrape')

# def scrape(name = "Microsoft", length=1):
#    result = wikipedia.summary(name, sentences=length)

#    click.echo(click.style(f"{result}:", fg="blue"))

# if __name__== '__main__':
    
#    scrape()