"Builder Menu"

from evennia.utils.evmenu import EvMenu
from commands.command import MuxCommand
from tables import GYGAX, rolltable

def new_room(caller):
    text = \
        """
        You entered an unfinished node. And rolled on 
        """
    options = ({"desc": "Accept Fate",
                "goto": "roll_passage"},
               {"desc": "Start in a room or chamber",
                "goto": "roll_chamber"})
    return text, options


class Cmd(MuxCommand):
    """
    Build command

    This is automatically called when you enter an unfinished node.

    """
    key = "@build"

    def func(self):
        '''
        '''

        results = rolltable(GYGAX, "I")  # rolls only on the periodic table.

        # Start Menu
        EvMenu(self.caller, "world.build_menu",
               startnode="new_room",
               cmdset_mergetype="Replace", cmdset_priority=1,
               auto_quit=True, auto_look=True, auto_help=True,
               cmd_on_exit="look",
               persistent=False,
               )


"""
nothing = EvMenu()

print nothing

return
"""
