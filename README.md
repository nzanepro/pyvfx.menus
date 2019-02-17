pyvfx.menus
==================

A package to find & import menu.py files in all packages colocated with this package.
Currently Works for Nuke and Maya.

I like the idea of using a virtual environment and pip to manage python packages for these DCC apps.
The latest version of pipenv handles this very nicely: https://github.com/pypa/pipenv

If you would like to contribute code for other dcc programs to use this system, please fork and create a pull request. 

set these environment variables so maya and nuke can load them appropriately:

maya uses the PYTHONPATH, and will load userSetup.py
nuke uses NUKE_PATH, and will load init.py

csh/tcsh example:
```tcsh
setenv NUKE_PATH "${NUKE_PATH}:${VIRTUAL_ENV}/lib/python2.7/site-packages"
setenv PYTHONPATH "${PYTHONPATH}:${VIRTUAL_ENV}/lib/python2.7/site-packages"
```
bash example:
```bash
export NUKE_PATH="${NUKE_PATH}:${VIRTUAL_ENV}/lib/python2.7/site-packages"
export PYTHONPATH="${PYTHONPATH}:${VIRTUAL_ENV}/lib/python2.7/site-packages"
```

see https://github.com/nzanepro/pyvfx.boilerplate for an example of a menu.py in use.
