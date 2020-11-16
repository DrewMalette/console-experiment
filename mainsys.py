# main system shell

import os, glob, importlib

def get_apps():
    os.chdir("apps")
    
    # seems redundant but this is to prevent an error
    #  on an intial run
    os.system("touch __init__.py")
    os.system("rm __init__.py")
    os.system("touch __init__.py") # clean slate
    files = glob.glob("*")
    for f in files:
        if os.path.isdir(f):
            os.system("echo 'from . import {}' >> __init__.py".format(f))
    
    os.chdir("..")
    
    #return files # needed?

print("Hello! Welcome to the Main System Shell!")

get_apps()

importlib.import_module("apps.game1")
#import apps.game1

