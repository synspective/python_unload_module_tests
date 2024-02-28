case "$1" in
    "setup")
        poetry install
        ;;
    "simple_test") # does not work
        poetry run pytest python_import_as_tests/tests/simple_test.py
        ;;
    "unload_function_test") # does not work
        poetry run pytest python_import_as_tests/tests/unload_function_test.py
        ;;
    "unload_module_test") # does not work
        poetry run pytest python_import_as_tests/tests/unload_module_test.py
        ;;
    "reload_test")
        poetry run pytest python_import_as_tests/tests/reload_test.py
        ;;
    "importlib_import_test")
        poetry run pytest python_import_as_tests/tests/importlib_import_test.py
        ;;
    "importlib_import_test_del")
        poetry run pytest python_import_as_tests/tests/importlib_import_test_del.py
        ;;
    "pytest_forked")
        poetry run pytest python_import_as_tests/tests/pytest_forked.py
esac
