import click

@click.group()
def request():
    pass

METHODS = ["GET", "POST", "PUT", "DELETE", "PATCH"]

@request.command()
@click.argument("method", type=click.Choice(METHODS))
@click.argument("url")
@click.option("-h", "--header", "headers", multiple=True, help="Cabecera tipo 'Key:Value', repetible")
@click.option("-p", "--param", "params", multiple=True, help="Query param tipo 'key:value', repetible")
@click.option("-d", "--data", "data_str", default=None, help="Body como string 'key:value,key2:value2' o usa --json")
@click.option("--json", "json_str", default=None, help="Body como string JSON crudo")
@click.option("-c", "--cookie", "cookies", multiple=True, help="Cookie tipo 'key:value', repetible")
@click.option("-t", "--timeout", default=10.0, type=float)
def send(method, url, headers, params, data_str, cookies, timeout):

    

