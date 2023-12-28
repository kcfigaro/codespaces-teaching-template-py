"""
This is the main python file for the calculator
"""
import click

from . import commands

#build a click group
@click.group()
def cli():
    """
    This is a command line calculator
    """
    pass

cli.add_command(commands.add_command)
cli.add_command(commands.subtract_command)
cli.add_command(commands.multiply_command)
cli.add_command(commands.divide_command)

