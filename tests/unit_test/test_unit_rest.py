from wzhang import rest
import os
import pytest


@pytest.fixture()
def mock_env_infile(monkeypatch):
    userdemo = "USERDEMO"
    monkeypatch.setenv(userdemo, "wzhang-demo-file", prepend=False)


# Use file fixture
def test_use_file_fixture(mock_env_infile):
    response = rest.hello_world()
    assert response == 'Hello, World!'
    assert os.getenv("USERDEMO") == "wzhang-demo-file"


# Use conftest.py fixture
def test_hello_world_rest(init_env):
    response = rest.hello_world()
    assert response == 'Hello, World!'
    assert os.getenv("USERDEMO") == "wzhang-demo"


class TestInClassLevel():
    # Use file fixture
    def test_fixture_in_class(self, mock_env_infile):
        response = rest.hello_world()
        assert response == 'Hello, World!'
        assert os.getenv("USERDEMO") == "wzhang-demo-file"
