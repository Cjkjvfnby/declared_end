import pytest


@pytest.fixture
def error_checker(caplog):
    def wrapper(*errors):
        actual = tuple(filter(None, caplog.text.split("\n")))[1:]
        assert actual == errors

    return wrapper
