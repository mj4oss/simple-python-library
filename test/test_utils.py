from simple_python_library.utils import hello, sum


def test_hello():
    assert hello("World") == "Hello, World!"
    assert hello("Alice") == "Hello, Alice!"
    assert hello("") == "Hello, !"

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0