"Builder Menu"

from evennia.utils.evmenu import EvMenu
from commands.command import MuxCommand
from tables import GYGAX, rolltable, gettable
# from evennia import search_object


def menunode_start(caller, table, override=None):
    (dieroll, name, desc, build_cmd) = rolltable(GYGAX, table, override)
    # table is a string name of a known table
    # override is optional and sets a particular result
    text = "You rolled a %s" % dieroll
    text += "\nresulting in a %s" % name
    text += "\n %s" % desc
    text += "\n Build recipe = "
    text += '\n'.join(build_cmd)

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


def _build_it(caller, build_cmd):
    caller.execute_cmd("@name here = Autobuilt room")
    default_desc = "This room built by AUTOBUILDER(TM)"
    caller.execute_cmd("@desc here = %s" % default_desc)


def menunode_end(caller):
    "End of the menu"
    text = "Reached End Node"
    return text, None


def menunode_table(caller, table_no):
    "Display table"
    table = gettable(GYGAX, table_no)
    # TODO make this work for all tables
    # title, die, list
    # list = name, desc, build

    # "I": ["PERIODIC CHECK", 20, [  # table name, die size
    #    (1, 2, "Continue Straight",  # low, high dice, result
    #       """
    #        -- check again in 60' (this table)""",  # desc
    #        ["@tun f", "@name here = Straight Passage"]),  # build list
    title = table[0]
    for i in table[2]:
        name = i[2]

    name = table[2][2]
    desc = table[[2][

    

    text = "A menu of all options on Table %s" % table_no
    options = ({"desc": tabledesc,
                "goto": None},
               {"key": "Chamber",
                "goto": None})

    return text, options


class CmdAutoBuild(MuxCommand):
    """
    Automatic Build command

    This is automatically called when you enter an unfinished node.

    Idea: with arguments you can choose a particular table and even over ride
    the die-roll or result. (two separate things)
    This means the command itself can be used to navigate the tables

    """
    key = "@autobuild"

    def func(self):
        '''
        '''

        table = self.rhs or None
        dieroll = self.lhs or None

        # Start Menu
        EvMenu(self.caller, "world.build_menu",
               startnode="menunode_start",
               cmdset_mergetype="Union", cmdset_priority=1,
               auto_quit=True, auto_look=True, auto_help=True,
               cmd_on_exit="look",
               persistent=False,
               table=table,
               dieroll=dieroll,
               )
