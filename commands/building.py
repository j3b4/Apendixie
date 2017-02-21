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
from evennia.utils import create
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
                  # "u": ("up", "d"),
                  # "d": ("down", "u"),
                  # "i": ("in", "o"),
                  # "o": ("out", "i")
                  # Don't want to use @tun for level changes etc.
                  }

    new_room_lockstring = "control:id({id}) or perm(Wizards); " \
                          "delete:id({id}) or perm(Wizards); " \
                          "edit:id({id}) or perm(Wizards)"

    def func(self):
        "Implements the tunnel command"

        caller = self.caller
        location = caller.location

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

        backstring = ""

        # later set more custome room types
        # esp to set context ie. "in a passage" v. "behind a door"
        roomclass = settings.BASE_ROOM_TYPECLASS
        doorclass = "typeclasses.doors.SimpleDoor"
        typeclass = ""
        # if not "oneway" in self.switches:
        if "door" in self.switches:
            roomname = "new space beyond a door (table II.b)"
            typeclass = doorclass
            exitname = "%s door" % exitname
            # exitshort = "%s:%s" % (exitshort, doorclass)
            backname = "%s door" % backname
        else:
            exitname = "%sern passage" % exitname
            backname = "%sern passage" % backname
            typeclass = settings.BASE_EXIT_TYPECLASS
        if "oneway" not in self.switches:
            backstring = ", %s;%s" % (backname, backshort)
            if "door" in self.switches:
                backstring = "%s:%s" % (backstring, doorclass)

        if self.rhs:
            roomname = self.rhs  # this may include aliases; that's fine.

        # TODO: Call the create room and exit commands

        # create the room
        new_room = create.create_object(roomclass, roomname, report_to=caller)
        lockstring = self.new_room_lockstring.format(id=caller.id)
        new_room.locks.add(lockstring)

        # tag it as unfinished
        if typeclass == doorclass:
            new_room.tags.add("unfinished")
            new_room.tags.add("afterdoor")
        else:
            new_room.tags.add("unfinished")
            new_room.tags.add("inpasage")

        # report to builder
        room_string = "Created room %s(%s)" % (new_room, new_room.dbref)

        # create exits to the room

        exit_to_string = ""
        exit_back_string = ""

        # If door  = then typeclass will match here.
        new_to_exit = create.create_object(typeclass, exitname, location,
                                           locks=lockstring,
                                           aliases=exitshort,
                                           destination=new_room,
                                           report_to=caller)
        new_to_exit.db.direction = exitshort
        alias_string = ""
        if new_to_exit.aliases.all():
            alias_string = " (%s)" % ", ".join(new_to_exit.aliases.all())
        exit_to_string = "\nCreated Exit from %s to %s: %s(%s)%s."
        exit_to_string = exit_to_string % (location.name,
                                           new_room.name,
                                           new_to_exit,
                                           new_to_exit.dbref,
                                           alias_string)

        # create back exits from room
        if "oneway" not in self.switches:
            new_back_exit = create.create_object(typeclass, backname, new_room,
                                                 aliases=backshort,
                                                 locks=lockstring,
                                                 destination=location,
                                                 report_to=caller)
            new_back_exit.db.direction = backshort
            alias_string = ""
            if new_back_exit.aliases.all():
                alias_string = " (%s)" % ", ".join(new_back_exit.aliases.all())
            exit_back_string = "\nCreated Exit back from %s to %s: %s(%s)%s."
            exit_back_string = exit_back_string % (new_room.name,
                                                   location.name,
                                                   new_back_exit,
                                                   new_back_exit.dbref,
                                                   alias_string)
        caller.msg("%s%s%s" % (room_string, exit_to_string, exit_back_string))

        # if inherits_from(new_exit, SimpleDoor):
        if "door" in self.switches:
            # link exits
            new_to_exit.db.return_exit = new_back_exit
            new_back_exit.db.return_exit = new_to_exit

# last line
