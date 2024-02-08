SUB_SETUP = False

def sub_setup():
    global SUB_SETUP
    if SUB_SETUP is False:
        SUB_SETUP = True
        return False
    else:
        return True
