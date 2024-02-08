def test_unload_function_one():
    from python_import_as_tests.my_package_main import setup
    assert setup() is False
    del setup

def test_unload_function_two():
    from python_import_as_tests.my_package_main import setup
    assert setup() is False
    del setup
