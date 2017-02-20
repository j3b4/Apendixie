"""
Commands that allow players to update their own journal attribute
"""

from commands.command import MuxCommand
from evennia.utils.gametime import gametime


class CmdUpdateJournal(MuxCommand):
    """
    Update your own journal

    Usage:
        +journal <Your entry>

    This appends an entry to your character's journal, automatically recording
    the time, zone, and location.
    """

    key = "+journal"

    def func(self):
        "Updates the journal"
        caller = self.caller
        location = caller.location
        zone = "A Fake Dungeon"
        time = gametime()
        journal = caller.db.journal
        usage = "+journal <Your entry>"
        if not self.args:
            caller.msg(usage)
            return
        else:
            entry = self.lhs

        journal.append([time, zone, location, entry])
        caller.msg("Added to journal:\n%s" % entry)


class CmdReadJournal(MuxCommand):
    """
    Read your journal - raw output

    Usage:
        +read

    Displays the content of the player journal.
    """
    key = "+read"

    def func(self):
        caller = self.caller
        journal = caller.db.journal
        # remember order of elements in the log entry:
        # journal.append([time, zone, location, entry])
        if journal:
            for i in journal:
                caller.msg("%s: At %s in %s\n %s" % (i[0], i[2], i[1], i[3]))
        else:
            caller.msg("You have nothing in your journal")
