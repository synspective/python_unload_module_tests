# Can you unload a module between tests being runs

## Using vanilla Python: no
The tests import a module, which itself import a submodule. For each, we check if the module was already initialized in two tests.

I have tried different technics, they are available in the `python_import_as_tests/tests` folder.

For what it is worth, a quick Google search on looking at ways to unload a module also shows that the conscensus seems to say that it is not possible.

**It looks like Python modules are mostly thought out to be imported once. The objects they expose are not meant to be reset through another import.**

## Using pytest-forked

The `pytest-forked` package does reset the Python executable for every test, which means the global variables are reset between tests. However, I am still a bit weary about using this package because:
- It is in maintenance mode, and is even [marked as deprecated on libraries.io](https://libraries.io/pypi/pytest-forked)
- I am not fully aware of the consequences of starting an entire new fork of the interpreter. These feel wide ranging.
