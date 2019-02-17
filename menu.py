# entrypoint for nuke
import nuke
import nukescripts
from pyvfx.menus import activate

if nuke.GUI:
    nukescripts.utils.executeDeferred(activate)
