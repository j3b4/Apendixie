"""
Tables
these commands allow players to roll dice on a virtual replica of the Appendix
A tables from the AD&D DMG.
"""
# from evennia import Command as BaseCommand
from commands.command import MuxCommand
# from evennia.commands.default.muxcommand import MuxCommand as MuxCommand
from world.tables import xTABLE as tableset  # to be deprecated
from world.tables import GYGAX, rolltable
# from world.tables import rolltable
from random import randint
from textwrap import dedent


class CmdOldTable(MuxCommand):
    """
    Roll a d20 and compare results to a table. Tables are identified by their
    roman numeral heading in Appendix A.

    Usage:
        table [Numeral] [ = overide]

    This command returns the virtual die result and the descripttion.

    Examples:
        table           ----> prints a list of tables
        table II.a      ----> rolls a d20 on table II.a
        table II.a = 20 -----> overides the die roll and chooses the result 20

    Alias:
        tr

    """
    key = "oldtable"
    help_category = "Table Commands"
    usage = "usage: table [Numeral] [= <dice result>]"

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

        if overide:
            roll = int(overide)
        else:
            roll = randint(1, die_size)

        caller.msg("You rolled a %s on a d%s\n" % (roll,
                   die_size))
        caller.location.msg_contents("%s rolled a %s on a d%s\n" %
                                     (caller.name, roll, die_size),
                                     exclude=caller)
        caller.msg("You check Table %s" % tab_name)
        name = ""
        desc = ""
        build = ""

        # look up roll on the table
        for n in tableset[tab_no][3]:
            if n[0] <= roll and n[1] >= roll:
                name = n[2]
                if len(n) >= 4:
                    desc = dedent(n[3])
                if len(n) == 5:
                    build = dedent(n[4])
                break
        result = ("{C%s{n %s\n%s" % (name, desc, build))
        caller.msg(result)
        caller.location.msg_contents(result, exclude=caller)
        # print table
    pass


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
