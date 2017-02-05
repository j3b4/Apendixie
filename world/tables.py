# This file contains all the tables
# lets get one working
# table 1

# TODO: Note, that the die size collumns are arbitrary, so there is a risk of
# mismatch with the actual length of the table list. Fixing this would require
# a small patch to commands.tables.CmdTable

TABLES = [  # APPENDIX_A
    ["num.", "Table Name", ],
    ["I.", "PERIODIC CHECK", 20, [
        (1, 2, "Continue Straight", """
         -- check again in 60' (this table)"""),
        (3, 5, "Door",
            """
            (see Table II.) <roll on Table II.a first, then II.b>"""),
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
            (See Table V.) -- check 30' after leaving
            (this table)"""),
        (17, 17, "Stairs", "(see Table VI.)"),
        (18, 18, "Dead End",
            """
            (walls left, right, and ahead can be checked for Secret
            Doors, see Table V.D., footnote)"""),
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
        (11, 18, "Room", "(Go to Table V.room)"),
        (19, 20, "Chamber", "(Go to Table V.chamber)"),
        ]],
    ["III.", "SIDE PASSAGES", 20, [
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
    ["IV.", "TURNS", 20, [
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
    ["V.E.", "EXIT DIRECTION <<for passages only>>", 10, [
        # sneaking a d10 in here for lulz
        (1, 8, "straight ahead"),
        (9, 9, "45 degrees left/right*",
            """* The exit will be appropriate to existing circumstances, but
            use the direction before the slash in preference to the other."""),
        (10, 10, "45 degrees right/left*",
            """* The exit will be appropriate to existing circumstances, but
            use the direction before the slash in preference to the other."""),
    ]],
]  # END OF THE TABLE OF TABLES AKA APPENDIC A
