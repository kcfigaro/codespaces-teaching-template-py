"""
This is the function for calculator app
"""
import click


def add(first_term, second_term):
    """
    Function to add two numbers
    """
    return first_term + second_term

def subtract(first_term, second_term):
    """
    Function to subtract two numbers
    """
    return first_term - second_term

def multiply(first_term, second_term):
    """
    Function to multiply two numbers
    """
    return first_term * second_term

def divide(first_term, second_term):
    """
    Function to divide two numbers
    """
    return first_term / second_term

@click.command("add")
@click.argument("first_term", type=float)
@click.argument("second_term", type=float)
def add_command(first_term, second_term):
    """
    add two numbers
    """
    #Invoke add function with colored output from click
    click.echo(click.style("Result: {}".format(add(first_term, second_term)), fg="green"))

@click.command("subtract")
@click.argument("first_term", type=float)
@click.argument("second_term", type=float)
def subtract_command(first_term, second_term):
    """
    subtract two numbers
    """
    click.echo(click.style("Result: {}".format(subtract(first_term, second_term)), fg="red"))

@click.command("multiply")
@click.argument("first_term", type=float)
@click.argument("second_term", type=float)
def multiply_command(first_term, second_term):
    """
    multiply two numbers
    """
    click.echo(click.style("Result: {}".format(multiply(first_term, second_term)), fg="blue"))

@click.command("divide")
@click.argument("first_term", type=float)
@click.argument("second_term", type=float)
def divide_command(first_term, second_term):
    """
    divide two numbers
    """
    click.echo(click.style("Result: {}".format(divide(first_term, second_term)), fg="yellow"))
