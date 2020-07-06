import pytest
import os

@pytest.fixture
def init_env(monkeypatch):
    # Setup
    userdemo = "USERDEMO"
    monkeypatch.setenv(userdemo, "wzhang-demo", prepend=False)
    print("--Setup----" + os.getenv("%s" % userdemo) + "------\n")

    yield  # this is where the testing happens

    # Teardown
    monkeypatch.setenv(userdemo, "")
    print("--Teardown----" + os.getenv(userdemo) + "------\n")
