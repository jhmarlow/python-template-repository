from examplepackage.example_main import hello
from examplepackage.example_subpackage.example_module import example_func, return_one


def test_imports():
    hello()
    example_func()


def test_return_one():

    assert return_one == 2
