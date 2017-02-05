"""
Tables
these commands allow players to interact with the appendix directly.
"""
from commands.command import Command as BaseCommand
# from world.tables import TABLE_I
from world.tables import TABLES as tableset
from random import randint
# import re
# from evennia.contrib.dice import roll_dice as roll_dice


class CmdTable(BaseCommand):
    """
    Roll a d20 and compare results to a table

    Usage:
        table <I>

    This command returns the virtual die result and the descripttion. It then
    prompts the builder to place the determined room or exit.
    """
    key = "table"
    aliases = ["tr"]
    help_category = "Table Commands"
    usage = "table <number or label>"

    def func(self):
        caller = self.caller
        # caller.msg("Welcome. tableset = %s" % tableset)
        menu = "\n\n"
        if not self.args:
            for i in tableset:
                # print i
                menu += i[0]
                menu += ": "
                menu += i[1]
                menu += "\n"
            caller.msg(menu)
            return

        tab_name = self.args
        tab_name = tab_name.strip()
        # print "tab_name = %s" % tab_name

        tab_no = 0  # index of the target table

        for sublist in tableset:
            # print sublist[0]
            if tab_name == sublist[0]:
                # caller.msg("found %s. %s" % (tab_name, sublist[1]))
                break
                # this method stops with the first matching table name however
                # it would never know if I had duplicate table names.
                # would be good at load time to sanity check the whole table of
                # tables Appendix A.
            else:
                # print "no %s in there" % tab_name
                tab_no += 1  # update the counter
                # print "%s ==> tab no. [%s]" % (tab_name, tab_no)
        else:
            caller.msg(
                "'%s' is Not a known table. Please review the list using "
                "the 'table' command without arguments" % tab_name)
            # caller.msg(tableset)
            return

        caller.msg("You roll a d20 and check Table %s" % tab_name)

        roll = randint(1, 20)

        caller.msg("You rolled a %s\n-----------------\n" % roll)
        name = ""
        desc = ""

        # look up roll on the table
        for n in tableset[tab_no][2]:
            if n[0] <= roll and n[1] >= roll:
                name = n[2]
                desc = n[3]
                break
        result = ("%s: %s" % (name, desc))
        caller.msg(result)
        # print table
    pass
