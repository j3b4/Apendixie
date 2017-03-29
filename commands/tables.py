"""
Tables
these commands allow players to roll dice on a virtual replica of the Appendix
A tables from the AD&D DMG.
"""
# from evennia import Command as BaseCommand
from commands.command import MuxCommand
# from evennia.commands.default.muxcommand import MuxCommand as MuxCommand
# from world.tables import xTABLE as tableset  # to be deprecated
from world.tables import GYGAX, rolltable
# from world.tables import rolltable
from random import randint
from textwrap import dedent


class CmdTable(MuxCommand):
    """
    Roll a d20 and compare results to a table. Tables are identified by their
    roman numeral heading in Appendix A.

    Usage:
        table [Numeral] [ = overide]

    This command returns the virtual die result and the descripttion.

    Examples:
        table           ----> prints a list of tables (NOT FUNCTIONING NOW)
        table II.a      ----> rolls a d20 on table II.a
        table II.a = 20 -----> overides the die roll and chooses the result 20

    Alias:
        tr

    """
    key = "table"
    aliases = ["tr"]
    help_category = "Table Commands"
    usage = "usage: table [Numeral] [= <dice result>]"

    def func(self):
        caller = self.caller
        # caller.msg("Welcome. tableset = %s" % tableset)
        menu = "\n\n"
        if not self.args:
            menu = "No menu yet!"
            caller.msg(menu)
            # caller.msg(self.usage)
            return

        table_set = GYGAX
        table_no = self.lhs.strip()
        overide = self.rhs or None
        # print "tab_name = %s" % tab_name
        caller.msg("You check Table %s" % table_no)

        (name, desc, build) = rolltable(table_set, table_no, overide)
        # look up roll on the table
        result = ("{C%s{n %s\n%s" % (name, desc, build))
        caller.msg(result)
        caller.location.msg_contents(result, exclude=caller)
        # print table
    pass
