import os
import sys


try:
    import maya.cmds as cmds
    MAYA = True
except ImportError:
    MAYA = False

try:
    import nuke
    import nukescripts
    NUKE = True
except ImportError:
    NUKE = False


def _print(message):
    if NUKE:
        nuke.tprint(message)
    else:
        print(message)


def findMenus(pth):
    # input: path to search for menu.py file
    # returns list of modules
    results = []
    for dirName, subdirList, fileList in os.walk(pth):
        for fname in fileList:
            if fname == "menu.py" and dirName != pth:
                fullname = os.path.join(dirName, fname)
                for f, r in [(pth, ""), (".py", ""), (os.path.sep, ".")]:
                    fullname = fullname.replace(f, r)
                results.append(fullname[1:])
    return results


def importMenu(pth):
    _print("importing {}".format(pth))
    exec("import {}".format(pth))


def activate():
    # install location is parent directory of this package
    pyvfx_location = os.path.dirname(os.path.dirname(__file__))
    if pyvfx_location not in sys.path:
        _print("adding pyvfx location: {}".format(pyvfx_location))
        sys.path.append(pyvfx_location)

    menus = findMenus(pyvfx_location)
    for menu in menus:
        importMenu(menu)
