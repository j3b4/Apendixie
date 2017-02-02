"""
Exits

Exits are connectors between Rooms. An exit always has a destination property
set and has a single command defined on itself with the same name as its key,
for allowing Characters to traverse the exit to its destination.

"""
from evennia import DefaultExit


class Exit(DefaultExit):
    """
    Exits are connectors between rooms. Exits are normal Objects except
    they defines the `destination` property. It also does work in the
    following methods:

     basetype_setup() - sets default exit locks (to change, use
     `at_object_creation` instead).  at_cmdset_get(**kwargs) - this is called
     when the cmdset is accessed and should
                              rebuild the Exit cmdset along with a command
                              matching the name of the Exit object.
                              Conventionally, a kwarg `force_init` should force
                              a rebuild of the cmdset, this is triggered by the
                              `@alias` command when aliases are changed.
     at_failed_traverse() - gives a default error message ("You cannot
                            go there") if exit traversal fails and an
                            attribute `err_traverse` is not defined.

    Relevant hooks to overload (compared to other types of Objects):
        at_traverse(traveller, target_loc) - called to do the actual traversal
        and calling of the other hooks.
                                    If overloading this, consider using super()
                                    to use the default movement implementation
                                    (and hook-calling).
        at_after_traverse(traveller, source_loc) - called by at_traverse just
                            after traversing.
        at_failed_traverse(traveller) - called by at_traverse if traversal
                            failed for some reason. Will not be called if the
                            attribute `err_traverse` is defined, in which case
                            that will simply be echoed.
    """
    pass


class NewExit(DefaultExit):
    """
    When a rooms is being rolled up, and it is determined that it will have
    exits, every new exit except for the return exit - the direction the player
    arrived from, will be a "new exit" - the destination for every "new exit"
    is a "random node"

    """

    def at_object_creation(self):
        # new exits have special destination property
        self.destination = self.location.location
        # starting location is a builder so use their location
        pass

    def at_traverse(self, traveller, target_loc):
        # is this right?
        # or should the command be tweaked instead?
        # create a random node
        self.location.msg_contents(
            "%s traverses the %s." % (traveller, self.name)
            )
        pass
