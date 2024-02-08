def test_unload_module_one():
    from python_import_as_tests import my_package_main
    assert my_package_main.setup() is False
    del my_package_main

def test_unload_module_two():
    from python_import_as_tests import my_package_main
    assert my_package_main.setup() is False
    del my_package_main
