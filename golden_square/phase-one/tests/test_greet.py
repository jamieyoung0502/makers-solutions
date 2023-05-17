from lib.greet import greet


def test_greetings_to_adrian():
    greet_output = greet("Adrian")
    assert greet_output == "Hello, Adrian!"
