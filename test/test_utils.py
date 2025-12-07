from simple_python_library.utils import hello

def test_hello():
    assert hello("World") == "Hello, World!"
    assert hello("Alice") == "Hello, Alice!"
    assert hello("") == "Hello, !"
