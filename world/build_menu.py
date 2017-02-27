"Builder Menu"

from evennia.utils.evmenu import EvMenu
from commands.command import MuxCommand
from tables import GYGAX, rolltable


def menunode_start(caller):
    (name, desc, build) = rolltable(GYGAX, "I")
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
        -----
        """

    options = ({"key": ("A", "a"),
                "desc": "Accept Destiny's Edict",
                "exec": lambda caller:
                        caller.execute_cmd("@name here = Autobuiltroom"),
                "goto": "menunode_end"},
               {"key": ("F", "f"),
                "desc": "Flout fickle Fortune",
                "goto": "menunode_table_I"},
               {"key": ("C", "c"),
                "desc": "Cancel and move back",
                "exec": lambda caller:
                        caller.execute_cmd("move back")})
    return text, options


def _cancel_it(caller, raw_string):
    text = "You tried to cancel and moved back"
    caller.execute_cmd("eat toast")
    caller.msg(text)
    # return menunode_end


def _build_it(caller, raw_string):
    text = "This would build something"
    caller.execute_cmd("howdy fok")
    caller.msg(text)
    # return menunode_end


def menunode_end(caller):
    "End of the menu"
    text = "You have finished here"
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
               cmdset_mergetype="Replace", cmdset_priority=1,
               auto_quit=True, auto_look=True, auto_help=True,
               cmd_on_exit="look",
               persistent=False,
               )
