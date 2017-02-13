"""
Building  in Appendixie
"""
# TODO: attempting to overload the default @tunnel command
# from builtins import range

# import re
from django.conf import settings
# from django.db.models import Q
# from evennia.objects.models import ObjectDB
# from evennia.locks.lockhandler import LockException
# from evennia.commands.cmdhandler import get_and_merge_cmdsets
# from evennia.utils import create, utils, search
# from evennia.utils import create
# from evennia.utils.utils import inherits_from, class_from_module
from evennia.utils.utils import class_from_module
# from evennia.utils.eveditor import EvEditor
# from evennia.utils.spawner import spawn
# from evennia.utils.ansi import raw
# from evennia.commands.default.building import ObjManipCommand

COMMAND_DEFAULT_CLASS = class_from_module(settings.COMMAND_DEFAULT_CLASS)

# limit symbol import for API
# __all__ = ("ObjManipCommand", "CmdSetObjAlias", "CmdCopy",
#           "CmdCpAttr", "CmdMvAttr", "CmdCreate",
#           "CmdDesc", "CmdDestroy", "CmdDig", "CmdTunnel", "CmdLink",
#           "CmdUnLink", "CmdSetHome", "CmdListCmdSets", "CmdName",
#           "CmdOpen", "CmdSetAttribute", "CmdTypeclass", "CmdWipe",
#           "CmdLock", "CmdExamine", "CmdFind", "CmdTeleport",
#           "CmdScript", "CmdTag", "CmdSpawn")


class CmdTunnel(COMMAND_DEFAULT_CLASS):
    """
    create new rooms in cardinal directions only

    Usage:
      @tunnel[/switch] <direction> [= roomname[;alias;alias;...][:typeclass]]

    Switches:
      oneway - do not create an exit back to the current location
      tel - teleport to the newly created room
      door - Creates a Simple Door exit

    Example:
      @tunnel n
      @tunnel n = house;mike's place;green building

    This is a simple way to build using pre-defined directions:
     |wn,ne,e,se,s,sw,w,nw|n (north, northeast etc)
     |wu,d|n (up and down)
     |wi,o|n (in and out)
    The full names (north, in, southwest, etc) will always be put as
    main name for the exit, using the abbreviation as an alias (so an
    exit will always be able to be used with both "north" as well as
    "n" for example). Opposite directions will automatically be
    created back from the new room unless the /oneway switch is given.
    For more flexibility and power in creating rooms, use @dig.
    """

    key = "@tunnel"
    aliases = ["@tun", "@door"]
    locks = "cmd: perm(tunnel) or perm(Builders)"
    help_category = "Building"

    # store the direction, full name and its opposite
    directions = {"n": ("north", "s"),
                  "ne": ("northeast", "sw"),
                  "e": ("east", "w"),
                  "se": ("southeast", "nw"),
                  "s": ("south", "n"),
                  "sw": ("southwest", "ne"),
                  "w": ("west", "e"),
                  "nw": ("northwest", "se"),
                  "u": ("up", "d"),
                  "d": ("down", "u"),
                  "i": ("in", "o"),
                  "o": ("out", "i")}

    def func(self):
        "Implements the tunnel command"

        if not self.args or not self.lhs:
            string = ("Usage: @tunnel[/switch] <direction>"
                      "[= roomname[;alias;alias;...][:typeclass]]")
            self.caller.msg(string)
            return
        if self.lhs not in self.directions:
            string = ("@tunnel can only understand the following directions:"
                      "%s.") % ",".join(sorted(self.directions.keys()))
            string += "\n(use @dig for more freedom)"
            self.caller.msg(string)
            return
        # retrieve all input and parse it
        exitshort = self.lhs
        exitname, backshort = self.directions[exitshort]
        backname = self.directions[backshort][0]

        roomname = "new space in passage (table I)"

        if self.cmdstring == "@door":
            self.switches.append("door")

        telswitch = ""
        if "tel" in self.switches:
            telswitch = "/teleport"
        backstring = ""
        doorclass = "typeclasses.doors.SimpleDoor"
        # if not "oneway" in self.switches:
        if "door" in self.switches:
            roomname = "new space beyond a door (table II.b)"
            exitname = "%s door" % exitname
            exitshort = "%s:%s" % (exitshort, doorclass)
            backname = "%s door" % backname
        else:
            exitname = "%sern passage" % exitname
            backname = "%sern passage" % backname
        if "oneway" not in self.switches:
            backstring = ", %s;%s" % (backname, backshort)
            if "door" in self.switches:
                backstring = "%s:%s" % (backstring, doorclass)

        if self.rhs:
            roomname = self.rhs  # this may include aliases; that's fine.

        # build the string we will use to call @dig
        digstring = "@dig%s %s = %s;%s%s" % (telswitch, roomname,
                                             exitname, exitshort, backstring)
        self.execute_cmd(digstring)

# last line
