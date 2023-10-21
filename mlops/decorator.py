import click

def greeting_dec(func):
    def decorated():
        print("have a nice day~!!")
        func()
    return decorated

@greeting_dec
@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")


if __name__ == '__main__':
    hello()