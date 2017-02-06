"""
Tables
these commands allow players to roll dice on a virtual replica of the Appendix
A tables from the AD&D DMG.
"""
# from evennia import Command as BaseCommand
from evennia.commands.default.muxcommand import MuxCommand as BaseCommand
from world.tables import TABLES as tableset
from random import randint


class CmdTable(BaseCommand):
    """
    Roll a d20 and compare results to a table. Tables are identified by their
    roman numeral heading in Appendix A.

    Usage:
        table [Numeral] [ = overide]

    This command returns the virtual die result and the descripttion.

    Examples:
        table           ----> prints a list of tables
        table II.a      ----> rolls a d20 on table II.a
        table II.a = 20 -----> overides the dices and chooses the result for 20

    Alias:
        tr

    """
    key = "table"
    aliases = ["tr"]
    help_category = "Table Commands"
    usage = "usage: table [<numeral>] [= <dice result>]"

    def func(self):
        caller = self.caller
        # caller.msg("Welcome. tableset = %s" % tableset)
        menu = "\n\n"
        if not self.args:
            for i in tableset:
                '''
                menu += i[0]
                menu += ": "
                menu += i[1]
                menu += "\n"
                '''
                menu += '{:<10}{}\n'.format(i[0], i[1])
            caller.msg(menu)
            # caller.msg(self.usage)
            return

        tab_name = self.lhs
        tab_name = tab_name.strip()
        overide = self.rhs
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

        die_size = tableset[tab_no][2]  # 3rd collumn has dice type number
        caller.msg("You roll a d%s and check Table %s" % (die_size, tab_name))

        if overide:
            roll = int(overide)
        else:
            roll = randint(1, die_size)

        caller.msg("You rolled a %s\n-----------------\n" % roll)
        name = ""
        desc = ""

        # look up roll on the table
        for n in tableset[tab_no][3]:
            if n[0] <= roll and n[1] >= roll:
                name = n[2]
                if len(n) == 4:
                    desc = n[3]
                break
        result = ("%s: %s" % (name, desc))
        caller.msg(result)
        # print table
    pass
