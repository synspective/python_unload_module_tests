def test_simple_one():
    from python_import_as_tests.my_package_main import setup
    assert setup() is False

def test_simple_two():
    from python_import_as_tests.my_package_main import setup
    assert setup() is False
