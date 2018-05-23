import os
import platform

o = platform.system()


def ckeck_platform():
    if o == 'Linux':
        os.system("export FLASK_APP=gui.py")

    elif o == 'Windows':
        os.system("set FLASK_APP=gui.py")
