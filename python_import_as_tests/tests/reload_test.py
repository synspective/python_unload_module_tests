from python_import_as_tests import my_package_main
from importlib import reload

def test_unload_module_one():
    reload(my_package_main)
    assert my_package_main.setup() is False
    assert my_package_main.sub_setup() is False

def test_unload_module_two():
    reload(my_package_main)
    assert my_package_main.setup() is False
    assert my_package_main.sub_setup() is False
