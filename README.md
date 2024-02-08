# Can you unload a module between tests being runs

It doesn't look like it is possible.

The tests import a module, which itself import a submodule. For each, we check if the module was already initialized in two tests.

I have tried different technics, they are available in the `python_import_as_tests/tests` folder.

For what it is worth, a quick Google search on looking at ways to unload a module also shows that the conscensus seems to say that it is not possible.

I have also searched for solution with pytests, but that did not yield much results.

**It looks like Python modules are mostly thought out to be imported once. The objects they expose are not meant to be reset through another import.**
