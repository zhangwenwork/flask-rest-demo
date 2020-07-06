from wzhang import rest


def test_hello_world_rest():
    response = rest.hello_world()
    assert response == 'Hello, World!'

