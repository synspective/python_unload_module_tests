import pytest

@pytest.mark.forked
def test_one():
    from python_import_as_tests.my_package_main import setup
    assert setup() is False

@pytest.mark.forked
def test_two():
    from python_import_as_tests.my_package_main import setup
    assert setup() is False
