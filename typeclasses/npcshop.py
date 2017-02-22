# Apendixie/typeclasses/npcshop.py

from evennia.utils import evmenu

# Interesting, this is the first time I've started a  module in the typeclasses
# folder that didn't start with a class declaration.


def menunode_shopfront(caller):
    "This is the top-menu screen."

    shopname = caller.location.key
    wares = caller.location.db.storeroom.contents

    # Wares includes all items inside the storeroom, including the door! Let's
    # remove that from out for sale list.
    wares = [ware for ware in wares if ware.key.lower() != "door"]

    text = "*** Welcome to %s! ***\n" % shopname
    if wares:
        text += "   Things for sale (choose 1-%i to inspect);" \
                "\n[q]uit to exit:" % len(wares)
    else:
        text += "   There is nothing for sale"

    options = []
    for ware in wares:
        # add an option for every ware in store
        options.append({"desc": "%s (%s gold)" %
                       (ware.key, ware.db.gold_value or 1),
                        "goto": "menunode_inspect_and_buy"})

    return text, options


def menunode_inspect_and_buy(caller, raw_input):
    "Sets up the buy menu screen."

    wares = caller.location.db.storeroom.contents
    # remember we need to remove that pesky door again
    wares = [ware for ware in wares if ware.key.lower() != "door"]
    iware = int(raw_input) - 1  # menu selection minu 1 eq index of ware
    ware = wares[iware]
    value = ware.db.gold_value or 1  # good to learn about use "or" like this
    wealth = caller.db.gold or 0
    text = "You inspect %s:\n\n%s" % (ware.key, ware.db.desc)

    def buy_ware_result(caller):
            "This will be executed first when choosing to buy."
            rtext = "You pay %i gold and purchase %s!" % \
                    (value, ware.key)
            caller.db.gold -= value
            ware.move_to(caller, quiet=True)
            caller.msg(rtext)

    # evaluate the money situation, only offer a chance to buy if the PC has
    # enough wealth
    options = []
    if wealth >= value:
        options.append({"key": ("B", "b", "buy", "Buy"),
                        "desc": "Buy %s for %s gold" %
                        # (ware.key, ware.db.gold_value or 1),
                        (ware.key, value),
                        "goto": "menunode_rethink",
                        "exec": buy_ware_result})
    else:
        # cannot afford it
        text += "\n\nYou only have %i gold, " % wealth
        text += "and cannot afford the %s at %i gold" % (ware.key, value)

    options.append({"key": ("K", "k"),
                    "desc": "Keep shopping",
                    "goto": "menunode_shopfront"})
    options.append({"key": ("Q", "q"),
                    "desc": "Quit shopping",
                    "goto": "end_node"})
    return text, options


def menunode_rethink(caller, raw_input):
    "After buying or failing to buy a ware, decide what to do"
    text = ""

    options = ({"key": ("K", "k"),
                "desc": "Keep shopping",
                "goto": "menunode_shopfront"},
               {"key": ("Q", "Quit", "quit", "q"),
                "desc": "Quit shopping",
                "goto": "end_node"})
    return text, options


def end_node(caller):
    text = ""
    return text, None


# implement a command to open the shop
from commands.command import Command


class CmdBuy(Command):
    """
    Start to do some shopping

    Usage:
        buy
        shop
        browse

    This will allow you to browse the wares of the
    current shop and buy items you want.
    """
    key = "buy"
    aliases = ("shop", "browse")

    def func(self):
        "Starts the shop EvMenu instance"
        evmenu.EvMenu(self.caller,
                      "typeclasses.npcshop",
                      startnode="menunode_shopfront")

# set up the Comand Set
from evennia import CmdSet


class ShopCmdSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(CmdBuy())

# build a shop typeclass
from evennia import DefaultRoom, DefaultExit, DefaultObject
from evennia.utils.create import create_object


# class for front shop room
class NPCShop(DefaultRoom):
    def at_object_creation(self):
        # we could also use add(ShopCmdSet, permanent=True)
        self.cmdset.add_default(ShopCmdSet)
        self.db.storeroom = None


# command to build a complete shop (the Command base class
# should already have been imported earlier in this file)
class CmdBuildShop(Command):
    """
    Build a new shop

    Usage:
        @buildshop shopname

    This will create a new NPCshop room
    as well as a linked store room (named
    simply <storename>-storage for the
    wares on sale. The store room will be
    accessed through a locked door in
    the shop.
    """
    key = "@buildshop"
    locks = "cmd:perm(Builders)"
    help_category = "Builders"

    def func(self):
        "Create the shop rooms"
        if not self.args:
            self.msg("Usage: @buildshop <storename>")
            return
        # create the shop and storeroom
        shopname = self.args.strip()
        shop = create_object(NPCShop,
                             key=shopname,
                             location=None)
        storeroom = create_object(DefaultRoom,
                                  key="%s-storage" % shopname,
                                  location=None)
        shop.db.storeroom = storeroom
        # create a door between the two
        shop_exit = create_object(DefaultExit,
                                  key="back door",
                                  aliases=["storage", "store room"],
                                  location=shop,
                                  destination=storeroom)
        storeroom_exit = create_object(DefaultExit,
                                       key="door",
                                       aliases=["shop", "back", "out"],
                                       location=storeroom,
                                       destination=shop)
        # make a key for accessing the store room
        storeroom_key_name = "%s-storekey" % shopname
        storeroom_key = create_object(DefaultObject,
                                      key=storeroom_key_name,
                                      location=shop)
        # only allow chars with this key to enter the store room
        shop_exit.locks.add("traverse:holds(%s)" % storeroom_key_name)

        # inform the builder about progress
        message = "The shop %s was created!" % shop
        message += "\ndoors: %s, %s to %s created as well." % \
            (shop_exit, storeroom_exit, storeroom)
        message += "Use %s to enter the storeroom." % storeroom_key
        self.caller.msg(message)

# end of npcshop.py
