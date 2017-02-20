"""
Movement commands.
Most movement is conducted by using exits. But some types of movement like
relative directions require some operations in advance.
Will see where this goes.
"""

from commands.command import MuxCommand
from world.directions import turn


class CmdMove(MuxCommand):
    """
    Move the character through an exit relative to the characters current
    facing.

    move right
    """

    key = "move"
    alias = "mv"

    directions = {
        'forward': 'f',
        'forward right': 'fr',
        'right': 'r',
        'back right': 'br',
        'back': 'b',
        'back left': 'bl',
        'left': 'l',
        'forward left': 'fl'
        }

    def func(self):
        'turns and moves the character through an exit'
        if not self.args or not self.lhs:
            string = "Usage: move <direction>"
            self.caller.msg(string)
            return
        if self.lhs not in self.directions:
            string = ("you can only move in the following directions:"
                      "%s.") % ",".join(sorted(self.directions.keys()))
            self.caller.msg(string)
            return
        face = self.caller.db.direction
        move = self.args
        exit = turn(face, move)
        self.caller.execute_cmd(exit)
'''
'''
