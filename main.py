#!/usr/bin/env python
import click
from src import scraper

@click.group()
def cli():
    pass

@cli.command()
@click.argument('queryname', required=True)
def search(queryname):
    scraper.Scraper(queryname).print_results()

if __name__ == '__main__':
    cli()
