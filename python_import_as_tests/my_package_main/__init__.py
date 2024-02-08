from python_import_as_tests.my_package_main.submodule import sub_setup
SETUP = False

def setup():
    global SETUP
    if SETUP is False:
        SETUP = True
        return False
    else:
        return True

def run_subsetup():
    return sub_setup()
