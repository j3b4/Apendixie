"Builder Menu"

from evennia.utils.evmenu import EvMenu
from commands.command import Command


def new_room(caller):
    text = \
        """
        You're on a new node. You need to
        run the random room generator!
        """
    options = ({"desc": "Start in a passageway",
                "goto": "roll_passage"},
               {"desc": "Start in a room or chamber",
                "goto": "roll_chamber"})
    return text, options


class CmdTestMenu(Command):
    """
    Test menu

    usage test menu <menumodule>
    """
    key = "testmenu"

    def func(self):
        '''
        if not self.args:
            self.caller.msg("Usage: testmenu menumodule")
            return
        '''
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
