# entrypoint for maya

import maya.utils
from pyvfx.menus import activate

maya.utils.executeDeferred(activate)
