"Builder Menu"

from evennia.utils.evmenu import EvMenu
from commands.command import MuxCommand
from tables import GYGAX, rolltable
# from evennia import search_object


def menunode_start(caller):
    (name, desc, build_cmd) = rolltable(GYGAX, "I")
    # rolls only on the periodic table.
    text = \
        """
        You entered an unfinished node. And rolled on table I
        "Periodic Check".
        """
    text += "\nYou rolled: %s" % name
    text += "\n %s" % desc
    text += \
        """
        That suggest you will use this command:

        """
    text += build_cmd
    build_cmd = "@tun_f"

    options = ({"key": ("A", "a"),
                "desc": "Accept Destiny's Edict",
                "exec": _build_it(caller, build_cmd),
                "goto": "menunode_end"},
               {"key": ("F", "f"),
                "desc": "Flout fickle Fortune",
                "goto": "menunode_table_I"},
               {"key": ("C", "c"),
                "desc": "Cancel and move back",
                "exec": _cancel_it})
    return text, options


def _cancel_it(caller):
    text = "You tried to cancel and moved back"
    caller.execute_cmd("say I say I say")
    caller.msg(text)
    # return menunode_end


def _build_it(caller, build_cmd=None):
    caller.execute_cmd("@name here = Autobuilt room")
    default_desc = "This room built by AUTOBUILDER(TM)"
    caller.execute_cmd("@desc here = %s" % default_desc)


def menunode_end(caller):
    "End of the menu"
    text = "Reached End Node"
    return text, None


def continue_straight(caller):
    pass


def build_chamber(caller):
    pass


def menunode_table_I(caller):
    "Display table_I"
    # TODO make this work for all tables
    text = "A menu of all options on Table I"
    options = ({"key": "Continue straight",
                "goto": continue_straight},
               {"key": "Chamber",
                "goto": build_chamber})

    return text, options


class CmdAutoBuild(MuxCommand):
    """
    Automatic Build command

    This is automatically called when you enter an unfinished node.

    """
    key = "@autobuild"

    def func(self):
        '''
        '''

        # Start Menu
        EvMenu(self.caller, "world.build_menu",
               startnode="menunode_start",
               cmdset_mergetype="Union", cmdset_priority=1,
               auto_quit=True, auto_look=True, auto_help=True,
               cmd_on_exit="look",
               persistent=False,
               )
