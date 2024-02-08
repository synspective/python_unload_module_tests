from importlib import import_module

def test_unload_module_one():
    mod = import_module("python_import_as_tests.my_package_main")
    assert mod.setup() is False
    assert mod.sub_setup() is False
    del mod

def test_unload_module_two():
    mod = import_module("python_import_as_tests.my_package_main")
    assert mod.setup() is False
    assert mod.sub_setup() is False
    del mod
