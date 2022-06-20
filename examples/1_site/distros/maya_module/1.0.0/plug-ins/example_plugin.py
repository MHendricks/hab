"""sampleCommand.py
Copied from https://help.autodesk.com/view/MAYAUL/2017/ENU/?guid=__files_GUID_85B1116E_F0C1_42AD_9CD4_30E936B6C7B8_htm
"""

import sys
import maya.OpenMayaMPx as OpenMayaMPx

k_plugin_cmd_name = 'myCommandName'


class MyCommandClass(OpenMayaMPx.MPxCommand):
    def doIt(self, args):  # noqa: N802
        pass


def cmd_creator():
    '''Create an instance of our command.'''
    return OpenMayaMPx.asMPxPtr(MyCommandClass())


def initializePlugin(mobject):  # noqa: N802
    '''Initialize the plug-in when Maya loads it.'''
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerCommand(k_plugin_cmd_name, cmd_creator)
    except Exception:
        sys.stderr.write('Failed to register command: ' + k_plugin_cmd_name)


def uninitializePlugin(mobject):  # noqa: N802
    '''Uninitialize the plug-in when Maya un-loads it.'''
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(k_plugin_cmd_name)
    except Exception:
        sys.stderr.write('Failed to unregister command: ' + k_plugin_cmd_name)
