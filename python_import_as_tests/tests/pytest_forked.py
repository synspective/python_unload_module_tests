import pytest
import os

@pytest.mark.forked
def test_one():
    assert "TEST" not in os.environ
    os.environ["TEST"] = "test_one"
    assert os.environ["TEST"] == "test_one"

    from python_import_as_tests.my_package_main import setup
    assert setup() is False

@pytest.mark.forked
def test_two():
    assert "TEST" not in os.environ
    os.environ["TEST"] = "test_two"
    assert os.environ["TEST"] == "test_two"

    from python_import_as_tests.my_package_main import setup
    assert setup() is False
