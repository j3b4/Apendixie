"Bugged menu - attempting to recreate my menu problem"

"""
Hypothesis: A looping menu will cache user input even though I didn't ask it
to.
"""


from evennia.utils.evmenu import EvMenu
from commands.command import MuxCommand

def men_start(caller):
    food = caller.ndb._menutree.food
    caller.ndb._menutree.food = None

    text = "this menu is bugged"
    if food:
        text += "\n you have some %s" % food
    if "raw" in food:
        text += "\n your %s is raw, cook it?" % food

    options = ({"key": ("C", "c"),
                "desc": "Cook this %s" % food,
                "goto": "menunode_end",
                "exec": _cook(caller, recipe),
                },
               {"key": ("C", "c"),
                "desc": "Cancel",
                "goto": "menunode_end"})
    return text, options


def _cook(caller, food):
    if "raw" in food:
        caller.msg("Cooking %s..." % food)
        cookedfood = food.replace('raw', 'cooked')
        caller.nbd._menutree.food = cookedfood
    
    

class CmdBugMenu(MuxCommand):
    """
    usage @cook raw <food>
    returns your <food> is cooked eat it or cook it more?
    """
    key = "@cook"

    def func(self):
        print "Bug Menu started"
        self.caller.msg("Bug menu started")

        if self.lhs:
            food = self.lhs
        else:
            self.caller.msg("usage @cook [raw] <food>")
            return

        # Start Menu
        EvMenu(self.caller,
               "world.buggedmenu",
               startnode="men_start",
               cmdset_mergetype="Union", cmdset_priority=1,
               auto_quit=True, auto_look=True, auto_help=True,
               cmd_on_exit="look",
               persistent=False,
               food=food,
               # override=override
               )
'''
