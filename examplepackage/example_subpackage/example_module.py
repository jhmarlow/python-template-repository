"""Module level docstring."""


def add_one(func):
    """Function level Docstring."""
    return func() + 1


@add_one
def return_one():
    """Function level Docstring."""
    return 1


def example_func():
    """Function level Docstring."""
    print("example function")
