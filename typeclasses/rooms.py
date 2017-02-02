"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    pass

class RandomNode(Room):
    """
    A random node is the destination of every "NewExit" it might be a room or a
    hallway.   

    Question - is a chamber/room a subset of random node?
    """

    """ 
    On entry
    When a player enters a RandomNode - it starts rolling up features
    from the tables.
    """
