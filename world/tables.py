# This file contains all the tables
# lets get one working
# table 1
# and a command to look up results on a table
from random import randint
from textwrap import dedent

# TODO: Note, that the die size collumns are arbitrary, so there is a risk of
# mismatch with the actual length of the table list.  Avoiding this would
# require some sort of a check.

# TODO: add in builder commands to the table results, replacing the hints.

xTABLE = [  # APPENDIX_A  # used by old "table" command deprecated
    ["Numeral", "Table Name", ],
    ["I", "PERIODIC CHECK", 20, [
        (1, 2, "Continue Straight",
            """
            -- check again in 60' (this table)""",
            """
            {gBuilder Notes:{nTry {w@name{n 'ing this room "passageway" then
            try {w@tunnel{n the direction you're going and name the next room
            "passageway as well. From that room {w@tunnel{n blindly into the
            next room and re-roll from there."""),
        (3, 5, "Door",
            """
            (see Table II.) <roll on Table II.a first, then II.b>"""
            """
            {gBuilder Notes:{nOnce you figure out the doors location, use the
            {w@door{n command to place a door in the appropriate direction.
            By default the door is open, go through it and roll on II.b to find
            out what's there."""),
        (6, 10, "Side Passage",
            """
            (see Table III.) -- check again in 30'
            (this table)"""),
        (11, 13, "Passage Turns",
            """
            (see Table IV., check width on Table III.)
            check again in 30' (this table)"""),
        (14, 16, "Chamber",
            """
            (See Table V.ch) -- check 30' after leaving
            (this table)"""),
        (17, 17, "Stairs", "(see Table VI.)"),
        (18, 18, "Dead End",
            """
            (walls left, right, and ahead can be checked for Secret
            Doors, see Table V.D., footnote) <<Actually no, that wont work so
            don't bother. It's just a dead end.>>
            """),
        (19, 19, "Trick/Trap",
            """
            (See Table VII.), passage continues -- check again in
            30' (this table)"""),
        (20, 20, "Wandering Monster",
            """
            -- check again immeditately to see what lies ahead
            so direction of monster's approach can be determined."""),
        ]],
    ["II.a", "LOCATION OF DOOR", 20, [
        (1, 6, "Left", "<door is on left side of passage>"),
        (7, 12, "Right", "<door is on right side of passage>"),
        (13, 20, "Ahead", "<passage comed to and end at this door>"),
        ]],
    ["II.b", "SPACE BEYOND DOOR", 20, [
        (1, 4, "Parallel passage**",
            """or 10' x 10' room if door is straight ahead."""),
        (5, 8, "Passage straight ahead"),
        (9, 9, "Passage 45 degrees ahead/behind***",
            """
            ***The direction will be appropriate to existing circumstances,
            but use the direction before the slash in preference to the
            other."""),
        (10, 10, "Passage 45 degrees behind/ahead***",
            """
            ***The direction will be appropriate to existing circumstances,
            but use the direction before the slash in preference to the
            other."""),
        (11, 18, "Room", "(Go to Table V.ro)"),
        (19, 20, "Chamber", "(Go to Table V.chamber)"),
        ]],
    ["III", "SIDE PASSAGES", 20, [
        (1, 2, "left 90 degrees"),
        (3, 4, "right 90 degrees"),
        (5, 5, "left 45 degrees ahead"),
        (6, 6, "right 45 degrees ahead"),
        (7, 7, "left 45 degrees behind (left 135 degrees)"),
        (8, 8, "right 45 degrees behind (right 135 degrees)"),
        (9, 9, "left curve 45 degrees ahead"),
        (10, 10, "right curve 45 degrees ahead"),
        (11, 13, "passage 'T's"),
        (14, 15, "passage 'Y's"),
        (16, 19, "four-way intersection"),
        (20, 20, "passage 'X's",
            """
            if present passage is horizontal or vertical it forms a fifth
            passage into the 'X'."""),
        ]],
    ["III.A", "PASSAGE WIDTH", 20, [
        (1, 12, "10'"),
        (13, 16, "20'"),
        (17, 17, "30'"),
        (18, 18, "5'"),
        (19, 20, "SPECIAL PASSAGE", "TABLE III.B"),
        ]],
    ["III.B", "SPECIAL PASSAGE", 20, [
        (1, 4, "40', columns down center"),
        (5, 7, "40', double row of columns"),
        (8, 10, "50', double row of columns"),
        (11, 12, ("50', columns 10' right and left support 10' wide upper "
                  "galleries 20' above"),
            """
            Stairs up to gallery will be at end of passage (1-15) or at
            beginning (16-20). In the former case if a stairway is indicated in
            or adjacent to the pasage it will replace the end stairs 50% (1-10)
            of the time and supplement 50% (11-20) of the time."""),
        (13, 15, "10' stream**",
            """ Streams bisect the passage. They will be bridged 75%(1-15) of
            the time and be an obstacle 25% (16-20) of the time."""),
        ]],
    ["IV", "TURNS", 20, [
        (1, 8, "left 90 degrees"),
        (9, 9, "left 45 degrees ahead"),
        (10, 10, "left 45 degrees behind", "(left 135 degrees)"),
        (11, 18, "right 90 degrees"),
        (19, 19, "right 45 degrees ahead"),
        (20, 20, "right 45 degrees behind", "(right 135 degrees)"),
        ]],
    ["V.ch", "CHAMBERS", 20, [
        (1, 2, "Square, 20' x 20'"),
        (3, 4, "Square, 20' x 20'"),
        (5, 6, "Square, 30' x 30'"),
        (7, 8, "Square, 40' x 40'"),
        (9, 10, "Rectangular, 20' x 30'"),
        (11, 13, "Rectangular, 20' x 30'"),
        (14, 15, "Rectangular, 30' x 50'"),
        (16, 17, "Rectangular, 40' x 60'"),
        (18, 20, "Unusual shape and size",
            """
            See subtables: V.A and V.B"""),
        ]],
    ["V.ro", "ROOM", 20, [
        (1, 2, "Square, 10' x 10'"),
        (3, 4, "Square, 20' x 20'"),
        (5, 6, "Square, 30' x 30'"),
        (7, 8, "Square, 40' x 40'"),
        (9, 10, "Rectangular, 10' x 20'"),
        (11, 13, "Rectangular, 20' x 30'"),
        (14, 15, "Rectangular, 20' x 40'"),
        (16, 17, "Rectangular, 30' x 40'"),
        (18, 20, "Unusual shape and size",
            """
            See subtables: V.A and V.B"""),
        ]],
    ["V.A", "UNUSUAL SHAPE", 20, [
        (1, 5, "Circular*",
            """
            * 1-5 has pool (See Table VIII.A and  VIII.C if appropriate),
            6-7 has well, 8-10 has shaft, and 11-20 is normal."""),
        (6, 8, "Triangular"),
        (9, 11, "Trapezoidal"),
        (12, 13, "Odd-Shaped**",
            """
            ** Draw what shape you desire or what will fit the map -- it is a
            special shape if desired. <<Describe the shape>>"""),
        (14, 15, "Oval"),
        (16, 17, "Hexagonal"),
        (18, 19, "Octagonal"),
        (20, 20, "Cave")
        ]],
    ["V.B", "UNUSUAL SIZE", 20, [
        (1, 3, "about 500 sq. ft."),
        (4, 6, "about 900 sq. ft."),
        (7, 8, "about 1,300 sq. ft."),
        (9, 10, "about 2,000 sq. ft."),
        (11, 12, "about 2,700 sq. ft."),
        (13, 14, "about 3,400 sq. ft."),
        (15, 20, "Roll again",
            """
            add the result to <2,000 sq. ft.> (if this generates another 15-20
            repeat the process, <adding another 2,000 sq. ft.>, and so on)"""),
        ]],
    ["V.C", "NUMBER <<and type>> OF EXITS", 20, [
        # Appendix A, TABLE V.C too tedious. This is a simplified version.
        (1, 4, "1 Door"),
        (5, 8, "1 Passage"),
        (9, 11, "2 Doors"),
        (11, 13, "1 Door, 1 Passage"),
        (14, 16, "2 Doors, 1 Passage"),
        (17, 18, "3 Doors"),
        (19, 19, "3 Doors, 1 Passage"),
        (20, 20, "0 Doors",
            """
            Check once per 10' for secret doors (see TABLE V.D., footnote)
            <<actually that wont help. So try this instead: Roll again on
            this chart and interpret any "Passage" result as a secret
            door. You're welcome."""),
        ]],
    ["V.D", "EXIT LOCATION", 20, [
        (1, 7, "opposite wall"),
        (8, 12, "left wall"),
        (13, 17, "right wall"),
        (18, 20, "same wall")
        ]],
    ["V.E", "EXIT DIRECTION <<for passages only>>", 10, [
        # sneaking a d10 in here for lulz
        (1, 8, "straight ahead"),
        (9, 9, "45 degrees left/right*",
            """* The exit will be appropriate to existing circumstances, but
            use the direction before the slash in preference to the other."""),
        (10, 10, "45 degrees right/left*",
            """* The exit will be appropriate to existing circumstances, but
            use the direction before the slash in preference to the other."""),
        ]],
    ["V.F", "CHAMBER OR ROOM CONTENTS", 20, [
        (1, 12, "Empty"),
        (13, 14, "Monster only",
            """
            (determine on appropriate table from APPENDIX C: RANDOM MONSTER
            ENCOUNTERS, Dungeon Encounter Matrix)."""),
        (15, 17, "Monster and treasure",
            """
            Monster - see APPENDIX C: RANDOM MONSTER ENCOUNTERS, Dungeon
            Encounter Matrix.
            Treasure - see TABLE V.G <<Roll twice>>"""),
        (18, 18, "Special/Stairs",
            """<< Roll on TABLE V.F.i STAIRS>>"""),
        (19, 19, "Trick/Trap",
            """
            See TABLE VII"""),
        (20, 20, "Treasure",
            """
            (see TABLE V.G)""")
        ]],
    ["V.F.i", "Stairs", 20, [
        (1, 5, "Up  1 level."),
        (6, 6, "<<no comment, just roll again I guess>>"),
        (7, 8, "Up 2 levels"),
        (9, 14, "Down 1 level."),
        (15, 19, "Down 2 levels."),
        (20, 20, "Down 3 levels",
            """
            -- 2 flights of stairs and a slanting passageway.""")
        ]],
    ["V.G", "TREASURE*", 100, [
        (1, 25, "1,000 copper pieces/level"),
        (26, 50, "1,000 silver pieces/level"),
        (51, 65, "750 electrum pieces/level"),
        (66, 80, "250 gold pieces/level"),
        (81, 90, "100 platiunum pieces/level"),
        (91, 94, "1-4 gems/level"),
        (95, 97, "1 piece jewelry/level"),
        (98, 100, "Magic",
            """
            (Roll once on Magic Items Table)""")
        ]],
    ["V.H", "TREASURE IS CONTAINED IN", 20, [
        (1, 2, "Bags"),
        (3, 4, "Sacks"),
        (5, 6, "Small Coffers"),
        (7, 8, "Chests"),
        (9, 10, "Huge Chests"),
        (11, 12, "Pottery Jars"),
        (13, 14, "Metal Urns"),
        (15, 16, "Stone Containers"),
        (17, 18, "Iron Trunks"),
        (19, 20, "Loose")
        ]],
    ["V.I", "TREASURE IS GUARDED BY", 20, [
        (1, 2, "Contact poison on container"),
        (3, 4, "Contact poison on treasure"),
        (5, 6, "Poisoned needles in lock"),
        (7, 7, "Poisoned needles in handles"),
        (8, 8, "Spring darts firing from front of container"),
        (9, 9, "Spring darts firing from top of container"),
        (10, 10, "Spring darts firing from inside bottom of container"),
        (11, 12, "Blade scything across inside"),
        (13, 13, "Poisonous insects or reptiles living inside containter"),
        (14, 14, "Gas released by opening container"),
        (15, 15, "Trapdoor opening in front of container"),
        (16, 16, "Trapdoor opening 6' in front of container"),
        (17, 17, "Stone block dropping in front of container"),
        (18, 18, "Spears released from walls when container opened"),
        (19, 19, "Explosive Runes"),
        (20, 20, "Symbol")
        ]],
    ["V.J", "TREASURE IS HIDDEN BY/IN", 20, [
        (1, 3, "Invisibilty"),
        (4, 5, "Illusion (to change of hide appearance)"),
        (6, 6, "Secret space under container"),
        (7, 8, "Secret compartment in container"),
        (9, 9, "Inside ordinary item in plain view"),
        (10, 10, "Disguised to appear as something else"),
        (11, 11, "Under a heap of trash/dung"),
        (12, 13, "Under a loose stone in the floor"),
        (14, 15, "Behind a loose stone in the wall"),
        (16, 20, "In a secret room nearby")
        ]],
    ["VI", "STAIRS", 20, [
        (1, 5, "Down 1 level*",
            """
            * 1 in 20 has a door which closes egress for the day."""),
        (6, 6, "Down 2 levels**",
            """
            ** 2 in 20 has a door which closes egress for the day."""),
        (7, 7, "Down 3 levels***",
            """
            *** 3 in  20 has a door which closes egress for the day."""),
        (8, 8, "Up 1 level"),
        (9, 9, "Up dead end",
            """
            (1 in 6 chance to chute down 2 levels)"""),
        (10, 10, "Down dead end",
            """
            (1 in 6 chance to chute down 1 level)"""),
        (11, 11, "Chimney up 1 level",
            """
            passage continues, check again in 30'"""),
        (12, 12, "Chimney up 2 levels",
            """
            passage continues, check again in 30'"""),
        (13, 13, "Chimney down 2 levels",
            """
            passage continues, check again in 30'"""),
        (14, 16, "Trap door down 1 level",
            """
            passage continues, check again in 30'"""),
        (17, 17, "Trap door down 2 levels",
            """
            passage continues, check again in 30'"""),
        (18, 20, "Up 1 then down 2",
            """
            (total down 1), chamber at end roll on TABLE V.)"""),
        ]],
    ["VII", "TRICK/TRAP", 20, [
        (1, 5, "Secret Door",
            """
            unless unlocated:  Non-elf locates 3 in 20, elf locates 5 in
            20, magical device locates 18 in 20 (then see TABLE II.). Unlocated
            secret doors = <<Pit 10' deep, 3 in 6 to fall in.>>"""),
        (6, 7, "Pit 10' deep",
            """
            3 in 6 to fall in."""),
        (8, 8, "Pit 10' deep",
            """
            with spikes, 3 in 6 to fall in."""),
        (9, 9, "20' x 20' elevator room",
            """
            (party has entered door directly ahead and is in room), descends
            1 level and will not ascend for 30 turns."""),
        (10, 10, "20' x 20' elevator room",
            """
            (party has entered door directly ahead and is in room), descends
            2 level and will not ascend for 30 turns."""),
        (11, 11,  "20' x 20' elevator room",
            """
            (party has entered door directly ahead and is in room), descends
            2-5 levels -- 1 upon entering and 1 additional level each time an
            unsuccessful attempt at door opening is made, or until it descends
            as far as it can. This will not ascend for 60 turns."""),
        (12, 12, "Wall",
            """
            10' behind slides across passage blocking it for 40-60 turns."""),
        (13, 13, "Oil",
            """
             (equal to one flask) pours on random person from hole in ceiling,
             followed by flaming cinder (2-12 h.p. damage unless successful
             save vs. magic is made, which indicates only 1-3 h.p.
             damage)."""),
        (14, 14, "Pit 10' deep, 3 in 6 to fall in.",
            """
            Pit walls move together to crush victim(s) in 2-5 rounds."""),
        (15, 15, "Arrow trap",
            """
            1-3 Arrows, 1 in 20 is poisoned."""),
        (16, 16, "Spear Trap",
            """
            1-3 spears, 1 in 20 is poisoned."""),
        (17, 17, "Gas",
            """
            Party has detected it, but must breathe it to continue along
            corridor, as it covers 60' ahead. Mark map accordingly regardless
            of turning back or not. (See TABLE VII.A)"""),
        (18, 18, "Door falls outward",
            """
            Causes 1-10 hit points, or stone falls from ceiling causing 2-20
            hit points of damage to each person failing their saving throw
            versus petrification."""),
        (19, 19, "Illusionary wall",
            """ ... concealing 8. (pit) above 1-6, 20. (chute) below (7-10)
            or chamber with monster and treasure (11-20)
            (see TABLE V.)."""),
        (20, 20, "Chute",
            """
            down 1 level (cannot be ascended in any manner)."""),
        # TODO: FINISH THIS
        ]],
    ["VII.A", "GAS SUB_TABLE", 20, [
        (1, 7, "Only effect is to obscure vision when passing through."),
        (8, 9, "Blinds for 1-6 turns after passing through."),
        (10, 12, "Fear",
            """
            Run back 120' feet unless saving throw versus magic is made."""),
        (13, 13, "Sleep",
            """
            Party sound asleep for 2-12 turns (as sleep spell)."""),
        (14-18, "Strength",
            """
            Adds 1-6 points of strength (as strength spell) to all fighters in
            the party for 1 to 10 hours."""),
        (19, 19, "Sickness",
            """
            Return to surface immediately."""),
        (20, 20, "Poison",
            """
            Killed unless saving throw versus poison is made.""")
        ]],
    ["VIII", "CAVES AND CAVERNS", 20, [
        (1, 5, "Cave about 40' x 60'"),
        (6, 7, "Cave about 50' x 75'"),
        (8, 9, "Double cave: 20' x 30', 60' x 60'"),
        (10, 11, "Double cave: 35' x 50', 80' X 90'"),
        (12, 14, "Cavern about 95' x 125' *",
            """
             * Roll to see if pool therein (see TABLE VIII.A.)."""),
        (15, 16, "Cavern about 120' x 150'"),
        (17, 18, "Cavern about 150' x 200' *",
            """
             * Roll to see if pool therein (see TABLE VIII.A.)."""),
        (19, 20, "Mammoth cavern about 250'-300' x 350'-400' **",
            """
            ** Roll to see if lake therein (see TABLE VIII.B.).""")
        ]],
    ["VIII.A", "POOLS", 10, [
        (1, 4, "No pool"),
        (5, 5, "Pool, no monster"),
        (6, 6, "Pool, monster"),
        (7, 9, "Pool, monster & treasure"),
        (10, 10, "Magical Pool *",
            """
            See TABLE VIII.C"""),
        ]],
    ["VIII.B", "LAKES", 10, [
        (1, 5, "No lake"),
        (6, 7, "Lake, no monsters"),
        (8, 9, "Lake, monsters. *",
            """
             * Determine monster and treasure from appropriate encounter
             matrix"""),
        (10, 10, "Enchanted Lake **",
            """
            ** Enchanted lake leads any who manage to cross it to another
            dimension, special temple, etc. (if special map is available,
            otherwise treat as lake with monsters), 90% chance that monster
            will guard lake.""")
        ]],
    ["VIII.C", "MAGIC POOLS", 20, [
        (1, 8, "<<Transmutation>>",
            """
            Turns gold to platinum (1-11) or lead (12-20), one time only."""),
        (9, 15, "Transfiguation",
            """
            Will, on a one-time only basis, add (1-3) or subtract (4-6) from
            one characteristic of all who stand within it:
            1 = strength     4 = dexterity
            2 = intelligence 5 = constitution
            3 = wisdom       6 = charisma
            (add or subtract from 1-3 points, checking for each character as to
            addition or subtraction, characteristic, and amount).
            """),
        (16, 17, "Talking Pool <<Wishes>>",
            """
             Talking pool which will grant 1 wish to characters of its
             alignment and damage others from 1-20 points. Wish can be withheld
             for up to 1 day. Pool's alignment is: lawful good 1-6, lawful evil
             7-9, chaotic good 10-12, chaotic evil 13-17, neutral 18-20."""),
        (19, 20, "Transporter pool:",
            """
             1-7, back to surface; 8-12, elsewhere on level; 13-16,
             1 level down; 17-20, 100 miles away for outdoor adventure.""")
        ]]
]  # END OF THE TABLE OF TABLES AKA APPENDIX A

GYGAX = {  # APPENDIX_A
    "I": ["PERIODIC CHECK", 20, [  # build ready
        (1, 2, "Continue Straight",  # low, high dice, result
            """
            -- check again in 60' (this table)""",  # desc
            ["@tun f", "@name here = Straight Passage"]),  # build list
        (3, 5, "Door",
            """
            (see Table II.) <roll on Table II.a first, then II.b>""",
            ["@autobuild II.a"]),  # build list
        (6, 10, "Side Passage",
            """
            (see Table III.) -- check again in 30'
            (this table)""",
            ["@autobuild III"]),
        (11, 13, "Passage Turns",
            """
            (see Table IV., check width on Table III.)
            check again in 30' (this table)""",
            ["@autobuild IV"]),  # build list of one item
        (14, 16, "Chamber",
            """
            (See Table V.ch) -- check 30' after leaving
            (this table)""",
            ["@autobuild V.ch"]),  # build list of one
        (17, 17, "Stairs", "(see Table VI.)", ["@autobuild VI"]),
        (18, 18, "Dead End",
            """
            (walls left, right, and ahead can be checked for Secret
            Doors, see Table V.D., footnote) <<Actually no, that wont work so
            don't bother. It's just a dead end.>>
            """,
            ["@name here = Dead End"]),
        (19, 19, "Trick/Trap",
            """
            (See Table VII.), passage continues -- check again in
            30' (this table)""",
            ["@create/drop Trick",
                "@tun f"]),
        (20, 20, "Wandering Monster",
            """
            -- check again immeditately to see what lies ahead
            so direction of monster's approach can be determined.""",
            ["@create/drop Monster",
                "@tun f"]),
        ]],
    "II.a": ["LOCATION OF DOOR", 20, [  # build ready
        (1, 6, "Left", "<door is on left side of passage>",
            ["@door l",
                "@tunnel f"]),
        (7, 12, "Right", "<door is on right side of passage>",
            ["@door r",
                "@tunnel f"]),
        (13, 20, "Ahead", "<passage comed to an end at this door>",
            ["@door f"]),
        ]],
    "II.b": ["SPACE BEYOND DOOR", 20, [  # TODO
        (1, 4, "Parallel passage**",
            """or 10' x 10' room if door is straight ahead."""),
        (5, 8, "Passage straight ahead"),
        (9, 9, "Passage 45 degrees ahead/behind***",
            """
            ***The direction will be appropriate to existing circumstances,
            but use the direction before the slash in preference to the
            other."""),
        (10, 10, "Passage 45 degrees behind/ahead***",
            """
            ***The direction will be appropriate to existing circumstances,
            but use the direction before the slash in preference to the
            other."""),
        (11, 18, "Room", "(Go to Table V.ro)"),
        (19, 20, "Chamber", "(Go to Table V.chamber)"),
        ]],
    "III": ["SIDE PASSAGES", 20, [  # build ready
        (1, 2, "Side Passage", "left 90 degrees",
            ["@tunnel f", "@tunnel l = dif passage"],),
        (3, 4, "Side Passage", "right 90 degrees",
            ["@tunnel f", "@tunnel r = dif passage"],),
        (5, 5, "Side Passage", "left 45 degrees ahead",
            ["@tunnel f", "@tunnel fl = dif passage"],),
        (6, 6, "Side Passage", "right 45 degrees ahead",
            ["@tunnel f", "@tunnel fr = dif passage"],),
        (7, 7, "Side Passage", "left 45 degrees behind (left 135 degrees)",
            ["@tunnel f", "@tunnel bl = dif passage"],),
        (8, 8, "Side Passage", "right 45 degrees behind (right 135 degrees)",
            ["@tunnel f", "@tunnel br = dif passage"],),
        (9, 9, "Curving Side Passage", "left curve 45 degrees ahead",
            ["@tunnel f", "@tunnel fl = dif passage"],),
        (10, 10, "Curving Side Passage", "right curve 45 degrees ahead",
            ["@tunnel f", "@tunnel fr = dif passage"],),
        (11, 13, "Junction", "passage 'T's",
            ["@tunnel l = dif passage", "@tunnel r = dif passage",
                "@name here = T intersection"],),
        (14, 15, "Junction", "passage 'Y's",
            ["@tunnel f", "@tunnel fl", "@tunnel fr",
                "@name here = Y Intersection"],),
        (16, 19, "Junction", "four-way intersection",
            ["@tunnel f", "@tunnel l", "@tunnel r",
                "@name here = Four way Intersection"],),
        (20, 20, "Junction", "passage 'X's",
            ["@tunnel fl", "@tunnel fr", "@tunnel bl", "@tunnel br",
                "@name here = Five way junction"],),
        ]],
    "III.A": ["PASSAGE WIDTH", 20, [  # hold
        # The idea is only call this upon entering a room named "dif passage"
        (1, 12, "10'", "new passage width",
            ["@desc = 10' wide passage"]),
        (13, 16, "20'", "new passage width",
            ["@desc = 20' wide passage"]),
        (17, 17, "30'", "new passage width",
            ["@desc = 30' wide passage"]),
        (18, 18, "5'", "new passage width",
            ["@desc = 5' wide passage"]),
        (19, 20, "SPECIAL PASSAGE", "TABLE III.B",
            ["@autobuild III.B"]),
        ]],
    "III.B": ["SPECIAL PASSAGE", 20, [  # hold
        (1, 4, "40', columns down center"),
        (5, 7, "40', double row of columns"),
        (8, 10, "50', double row of columns"),
        (11, 12, ("50', columns 10' right and left support 10' wide upper "
                  "galleries 20' above"),
            """
            Stairs up to gallery will be at end of passage (1-15) or at
            beginning (16-20). In the former case if a stairway is indicated in
            or adjacent to the pasage it will replace the end stairs 50% (1-10)
            of the time and supplement 50% (11-20) of the time."""),
        (13, 15, "10' stream**",
            """ Streams bisect the passage. They will be bridged 75%(1-15) of
            the time and be an obstacle 25% (16-20) of the time."""),
        ]],
    "IV": ["TURNS", 20, [  # build ready
        (1, 8, "left 90 degrees", "turn",
            ["@tunnel l",
                "@name here = Sharp Turn"]),
        (9, 9, "left 45 degrees ahead", "turn",
            ["@tunnel fl",
                "@name here = Slight Turn"]),
        (10, 10, "left 45 degrees behind", "(left 135 degrees)",
            ["@tunnel bl",
                "@name here = Hairpin Turn"]),
        (11, 18, "right 90 degrees", "turn",
            ["@tunnel l",
                "@name here = Sharp Turn"]),
        (19, 19, "right 45 degrees ahead", "turn",
            ["@tunnel r",
                "@name here = Slight Turn"]),
        (20, 20, "right 45 degrees behind", "(right 135 degrees)",
            ["@tunnel br",
                "@name here = Hairpin Turn"]),
        ]],
    "V.ch": ["CHAMBERS", 20, [
        (1, 2, "Square, 20' x 20'", "description",
            ["@name here = 20x20 Chamber",
                "@autobuild V.C"]),
        (3, 4, "Square, 20' x 20'", "description",
            ["@name here = 20x20 Chamber",
                "@autobuild V.C"]),
        (5, 6, "Square, 30' x 30'", "description",
            ["@name here = 20x20 Chamber",
                "@autobuild V.C"]),
        (7, 8, "Square, 40' x 40'", "description",
            ["@name here = 20x20 Chamber",
                "@autobuild V.C"]),
        (9, 10, "Rectangular, 20' x 30'", "description",
            ["@name here = 20x20 Chamber",
                "@autobuild V.C"]),
        (11, 13, "Rectangular, 20' x 30'", "description",
            ["@name here = 20x20 Chamber",
                "@autobuild V.C"]),
        (14, 15, "Rectangular, 30' x 50'", "description",
            ["@name here = 20x20 Chamber",
                "@autobuild V.C"]),
        (16, 17, "Rectangular, 40' x 60'", "description",
            ["@name here = 20x20 Chamber",
                "@autobuild V.C"]),
        (18, 20, "Unusual shape and size",
            """
            See subtables: V.A and V.B""",
            ["@autobuild V.A"]),
        ]],
    "V.ro": ["ROOM", 20, [  # hold - hope to deprecate this table soon
        (1, 2, "Square, 10' x 10'"),
        (3, 4, "Square, 20' x 20'"),
        (5, 6, "Square, 30' x 30'"),
        (7, 8, "Square, 40' x 40'"),
        (9, 10, "Rectangular, 10' x 20'"),
        (11, 13, "Rectangular, 20' x 30'"),
        (14, 15, "Rectangular, 20' x 40'"),
        (16, 17, "Rectangular, 30' x 40'"),
        (18, 20, "Unusual shape and size",
            """
            See subtables: V.A and V.B"""),
        ]],
    "V.A": ["UNUSUAL SHAPE", 20, [
        (1, 5, "Circular*",
            """
            * 1-5 has pool (See Table VIII.A and  VIII.C if appropriate),
            6-7 has well, 8-10 has shaft, and 11-20 is normal.""",
            ["@name here = Circular Room",
                "@autobuild V.B"]),
        (6, 8, "Triangular",
            ["@name here = Triangular Room",
                "@autobuild V.B"]),
        (9, 11, "Trapezoidal",
            ["@name here = Trapezoidal Room",
                "@autobuild V.B"]),
        (12, 13, "Odd-Shaped**",
            """
            ** Draw what shape you desire or what will fit the map -- it is a
            special shape if desired. <<Describe the shape>>""",
            ["@name here = Odd Shaped Room"]),
        (14, 15, "Oval",
            ["@name here = Oval Room",
                "@autobuild V.B"]),
        (16, 17, "Hexagonal",
            ["@name here = Hexagonal Room",
                "@autobuild V.B"]),
        (18, 19, "Octagonal",
            ["@name here = Octoganal Room",
                "@autobuild V.B"]),
        (20, 20, "Cave", "Cave type room",
            ["@autobuild VIII"])
        ]],
    "V.B": ["UNUSUAL SIZE", 20, [
        (1, 3, "about 500 sq. ft."),
        (4, 6, "about 900 sq. ft."),
        (7, 8, "about 1,300 sq. ft."),
        (9, 10, "about 2,000 sq. ft."),
        (11, 12, "about 2,700 sq. ft."),
        (13, 14, "about 3,400 sq. ft."),
        (15, 20, "Roll again",
            """
            add the result to <2,000 sq. ft.> (if this generates another 15-20
            repeat the process, <adding another 2,000 sq. ft.>, and so on)"""),
        ]],
    "V.C": ["NUMBER <<and type>> OF EXITS", 20, [
        # Appendix A, TABLE V.C too tedious. This is a simplified version.
        (1, 1, "1 Door", "placement ahead", ["@door f"]),
        (2, 2, "1 Door", "placement right", ["@door f"]),
        (3, 3, "1 Door", "placement left", ["@door f"]),
        (5, 5, "1 Passage", "placement ahead", ["@tunnel f"]),
        (6, 6, "1 Passage", "placement right", ["@tunnel r"]),
        (7, 7, "1 Passage", "placement left", ["@tunnel l"]),
        (9, 9, "2 Doors", "placed left and right",
            ["@door r", "@door l"]),
        (10, 10, "2 Doors", "placed forward and right",
            ["@door r", "@door f"]),
        (11, 11, "2 Doors", "placed forward and left",
            ["@door l", "@door f"]),
        (12, 12, "1 Door, 1 Passage", "passage fwd & door right",
            ["@tunnel f", "@door r"]),
        (13, 13, "1 Door, 1 Passage", "passage fwd & door left",
            ["@tunnel f", "@door l"]),
        (14, 16, "2 Doors, 1 Passage", "passage fwd; doors left & right",
            ["@tunnel f", "@door l", "door r"]),
        (17, 18, "3 Doors", "on all walls",
            ["@door r", "@door l", "@door f"]),
        (19, 20, "0 Doors",
            """
            Check once per 10' for secret doors (see TABLE V.D., footnote)
            <<actually that wont help. So try this instead: Roll again on
            this chart and interpret any "Passage" result as a secret
            door. You're welcome.""",
            ["@desc here = There are no obvious exits besides the one you"
                "entered from"]),
        ]],
    "V.D": ["EXIT LOCATION", 20, [
        (1, 7, "opposite wall"),
        (8, 12, "left wall"),
        (13, 17, "right wall"),
        (18, 20, "same wall")
        ]],
    "V.E": ["EXIT DIRECTION <<for passages only>>", 10, [
        # sneaking a d10 in here for lulz
        (1, 8, "straight ahead"),
        (9, 9, "45 degrees left/right*",
            """* The exit will be appropriate to existing circumstances, but
            use the direction before the slash in preference to the other."""),
        (10, 10, "45 degrees right/left*",
            """* The exit will be appropriate to existing circumstances, but
            use the direction before the slash in preference to the other."""),
        ]],
    "V.F": ["CHAMBER OR ROOM CONTENTS", 20, [
        (1, 12, "Empty"),
        (13, 14, "Monster only",
            """
            (determine on appropriate table from APPENDIX C: RANDOM MONSTER
            ENCOUNTERS, Dungeon Encounter Matrix)."""),
        (15, 17, "Monster and treasure",
            """
            Monster - see APPENDIX C: RANDOM MONSTER ENCOUNTERS, Dungeon
            Encounter Matrix.
            Treasure - see TABLE V.G <<Roll twice>>"""),
        (18, 18, "Special/Stairs",
            """<< Roll on TABLE V.F.i STAIRS>>"""),
        (19, 19, "Trick/Trap",
            """
            See TABLE VII"""),
        (20, 20, "Treasure",
            """
            (see TABLE V.G)""")
        ]],
    "V.F.i": ["Stairs", 20, [
        (1, 5, "Up  1 level."),
        (6, 6, "<<no comment, just roll again I guess>>"),
        (7, 8, "Up 2 levels"),
        (9, 14, "Down 1 level."),
        (15, 19, "Down 2 levels."),
        (20, 20, "Down 3 levels",
            """
            -- 2 flights of stairs and a slanting passageway.""")
        ]],
    "V.G": ["TREASURE*", 100, [
        (1, 25, "1,000 copper pieces/level"),
        (26, 50, "1,000 silver pieces/level"),
        (51, 65, "750 electrum pieces/level"),
        (66, 80, "250 gold pieces/level"),
        (81, 90, "100 platiunum pieces/level"),
        (91, 94, "1-4 gems/level"),
        (95, 97, "1 piece jewelry/level"),
        (98, 100, "Magic",
            """
            (Roll once on Magic Items Table)""")
        ]],
    "V.H": ["TREASURE IS CONTAINED IN", 20, [
        (1, 2, "Bags"),
        (3, 4, "Sacks"),
        (5, 6, "Small Coffers"),
        (7, 8, "Chests"),
        (9, 10, "Huge Chests"),
        (11, 12, "Pottery Jars"),
        (13, 14, "Metal Urns"),
        (15, 16, "Stone Containers"),
        (17, 18, "Iron Trunks"),
        (19, 20, "Loose")
        ]],
    "V.I": ["TREASURE IS GUARDED BY", 20, [
        (1, 2, "Contact poison on container"),
        (3, 4, "Contact poison on treasure"),
        (5, 6, "Poisoned needles in lock"),
        (7, 7, "Poisoned needles in handles"),
        (8, 8, "Spring darts firing from front of container"),
        (9, 9, "Spring darts firing from top of container"),
        (10, 10, "Spring darts firing from inside bottom of container"),
        (11, 12, "Blade scything across inside"),
        (13, 13, "Poisonous insects or reptiles living inside containter"),
        (14, 14, "Gas released by opening container"),
        (15, 15, "Trapdoor opening in front of container"),
        (16, 16, "Trapdoor opening 6' in front of container"),
        (17, 17, "Stone block dropping in front of container"),
        (18, 18, "Spears released from walls when container opened"),
        (19, 19, "Explosive Runes"),
        (20, 20, "Symbol")
        ]],
    "V.J": ["TREASURE IS HIDDEN BY/IN", 20, [
        (1, 3, "Invisibilty"),
        (4, 5, "Illusion (to change of hide appearance)"),
        (6, 6, "Secret space under container"),
        (7, 8, "Secret compartment in container"),
        (9, 9, "Inside ordinary item in plain view"),
        (10, 10, "Disguised to appear as something else"),
        (11, 11, "Under a heap of trash/dung"),
        (12, 13, "Under a loose stone in the floor"),
        (14, 15, "Behind a loose stone in the wall"),
        (16, 20, "In a secret room nearby")
        ]],
    "VI": ["STAIRS", 20, [
        (1, 8, "Down 1 level*",
            "Create a random downer",
            ["@create/drop Stairs Down",
                "@tunnel f",
                "@name here = Stairs leading down"]),
        (9, 10, "Up Stairs", "Create a random upper",
            ["@create/drop Stairs Up",
                "@tunnel f",
                "@name here = Stairs leading up"]),
        (11, 12, "Chimney up",
            """
            passage continues, check again in 30'""",
            ["@create/drop Chimney Up",
                "@tunnel f",
                "@name here = Stairs leading up"]),
        (12, 13, "Chimney up",
            """
            passage continues, check again in 30'""",
            ["@create/drop Chimney Up",
                "@tunnel f",
                "@name here = Stairs leading up"]),
        (14, 17, "Trap door down",
            """
            passage continues, check again in 30'""",
            ["@create/drop Trapdoor Down",
                "@tunnel f",
                "@name here = Stairs leading up"]),
        (18, 20, "Up 1 then down 2",
            """
            (total down 1), chamber at end roll on TABLE V.)""",
            ["@create/drop Stairs Up", "@tunnel f",
                "@name here = Stairs leading up"]),
        ]],
    "VII": ["TRICK/TRAP", 20, [
        (1, 5, "Secret Door",
            """
            unless unlocated:  Non-elf locates 3 in 20, elf locates 5 in
            20, magical device locates 18 in 20 (then see TABLE II.). Unlocated
            secret doors = <<Pit 10' deep, 3 in 6 to fall in.>>"""),
        (6, 7, "Pit 10' deep",
            """
            3 in 6 to fall in."""),
        (8, 8, "Pit 10' deep",
            """
            with spikes, 3 in 6 to fall in."""),
        (9, 9, "20' x 20' elevator room",
            """
            (party has entered door directly ahead and is in room), descends
            1 level and will not ascend for 30 turns."""),
        (10, 10, "20' x 20' elevator room",
            """
            (party has entered door directly ahead and is in room), descends
            2 level and will not ascend for 30 turns."""),
        (11, 11,  "20' x 20' elevator room",
            """
            (party has entered door directly ahead and is in room), descends
            2-5 levels -- 1 upon entering and 1 additional level each time an
            unsuccessful attempt at door opening is made, or until it descends
            as far as it can. This will not ascend for 60 turns."""),
        (12, 12, "Wall",
            """
            10' behind slides across passage blocking it for 40-60 turns."""),
        (13, 13, "Oil",
            """
             (equal to one flask) pours on random person from hole in ceiling,
             followed by flaming cinder (2-12 h.p. damage unless successful
             save vs. magic is made, which indicates only 1-3 h.p.
             damage)."""),
        (14, 14, "Pit 10' deep, 3 in 6 to fall in.",
            """
            Pit walls move together to crush victim(s) in 2-5 rounds."""),
        (15, 15, "Arrow trap",
            """
            1-3 Arrows, 1 in 20 is poisoned."""),
        (16, 16, "Spear Trap",
            """
            1-3 spears, 1 in 20 is poisoned."""),
        (17, 17, "Gas",
            """
            Party has detected it, but must breathe it to continue along
            corridor, as it covers 60' ahead. Mark map accordingly regardless
            of turning back or not. (See TABLE VII.A)"""),
        (18, 18, "Door falls outward",
            """
            Causes 1-10 hit points, or stone falls from ceiling causing 2-20
            hit points of damage to each person failing their saving throw
            versus petrification."""),
        (19, 19, "Illusionary wall",
            """ ... concealing 8. (pit) above 1-6, 20. (chute) below (7-10)
            or chamber with monster and treasure (11-20)
            (see TABLE V.)."""),
        (20, 20, "Chute",
            """
            down 1 level (cannot be ascended in any manner)."""),
        # TODO: FINISH THIS
        ]],
    "VII.A": ["GAS SUB_TABLE", 20, [
        (1, 7, "Only effect is to obscure vision when passing through."),
        (8, 9, "Blinds for 1-6 turns after passing through."),
        (10, 12, "Fear",
            """
            Run back 120' feet unless saving throw versus magic is made."""),
        (13, 13, "Sleep",
            """
            Party sound asleep for 2-12 turns (as sleep spell)."""),
        (14-18, "Strength",
            """
            Adds 1-6 points of strength (as strength spell) to all fighters in
            the party for 1 to 10 hours."""),
        (19, 19, "Sickness",
            """
            Return to surface immediately."""),
        (20, 20, "Poison",
            """
            Killed unless saving throw versus poison is made.""")
        ]],
    "VIII": ["CAVES AND CAVERNS", 20, [
        (1, 5, "Cave about 40' x 60'"),
        (6, 7, "Cave about 50' x 75'"),
        (8, 9, "Double cave: 20' x 30', 60' x 60'"),
        (10, 11, "Double cave: 35' x 50', 80' X 90'"),
        (12, 14, "Cavern about 95' x 125' *",
            """
             * Roll to see if pool therein (see TABLE VIII.A.)."""),
        (15, 16, "Cavern about 120' x 150'"),
        (17, 18, "Cavern about 150' x 200' *",
            """
             * Roll to see if pool therein (see TABLE VIII.A.)."""),
        (19, 20, "Mammoth cavern about 250'-300' x 350'-400' **",
            """
            ** Roll to see if lake therein (see TABLE VIII.B.).""")
        ]],
    "VIII.A": ["POOLS", 10, [
        (1, 4, "No pool"),
        (5, 5, "Pool, no monster"),
        (6, 6, "Pool, monster"),
        (7, 9, "Pool, monster & treasure"),
        (10, 10, "Magical Pool *",
            """
            See TABLE VIII.C"""),
        ]],
    "VIII.B": ["LAKES", 10, [
        (1, 5, "No lake"),
        (6, 7, "Lake, no monsters"),
        (8, 9, "Lake, monsters. *",
            """
             * Determine monster and treasure from appropriate encounter
             matrix"""),
        (10, 10, "Enchanted Lake **",
            """
            ** Enchanted lake leads any who manage to cross it to another
            dimension, special temple, etc. (if special map is available,
            otherwise treat as lake with monsters), 90% chance that monster
            will guard lake.""")
        ]],
    "VIII.C": ["MAGIC POOLS", 20, [
        (1, 8, "<<Transmutation>>",
            """
            Turns gold to platinum (1-11) or lead (12-20), one time only."""),
        (9, 15, "Transfiguation",
            """
            Will, on a one-time only basis, add (1-3) or subtract (4-6) from
            one characteristic of all who stand within it:
            1 = strength     4 = dexterity
            2 = intelligence 5 = constitution
            3 = wisdom       6 = charisma
            (add or subtract from 1-3 points, checking for each character as to
            addition or subtraction, characteristic, and amount).
            """),
        (16, 17, "Talking Pool <<Wishes>>",
            """
             Talking pool which will grant 1 wish to characters of its
             alignment and damage others from 1-20 points. Wish can be withheld
             for up to 1 day. Pool's alignment is: lawful good 1-6, lawful evil
             7-9, chaotic good 10-12, chaotic evil 13-17, neutral 18-20."""),
        (19, 20, "Transporter pool:",
            """
             1-7, back to surface; 8-12, elsewhere on level; 13-16,
             1 level down; 17-20, 100 miles away for outdoor adventure.""")
        ]],
}  # END OF THE DICTIONARY of TABLES AKA APPENDIX A


def rolltable(table_set, table_no, overide=None):
    """
    This accepts an argument for tableset and for table. Currently there is
    only one tableset called "GYGAX" since it is based on GARY GYGAXs tables
    from the DMG.

    Later we might at other tables.

    rolltable accecpts as well a table argument wich is essentiall a subtable.

    """
    # confirm table exists
    table = gettable(table_set, table_no)

    if overide:
        roll = int(overide)
    else:
        die_size = table[1]
        roll = randint(1, die_size)

    name = ""
    desc = ""
    build = ""

    for n in table[2]:
        if n[0] <= roll and n[1] >= roll:
            name = n[2]
            if len(n) >= 4:
                desc = dedent(n[3])
            if len(n) == 5:
                build = (n[4])
            break
    results = (roll, name, desc, build)
    return results


def gettable(table_set, table_no):
    """
    This looks up a table and returns it to the caller
    """
    # confirm table exists
    if table_no not in table_set.keys():
        print "ERROR: %s does not exist in %s" % (table_no, table_set)
        return

    return table_set[table_no]
# end
