# This file contains all the tables
# lets get one working
# table 1

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
        # Doors location relative to passage
        (1, 6, "Left", "<door is on left side of passage>"),
        (7, 12, "Right", "<door is on right side of passage>"),
        (13, 20, "Ahead", "<passage comed to and end at this door>"),
        ]],
    ["II.b", "SPACE BEYOND DOOR", 20, [
        # space beyond door
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
        ]]
    ["IV.", "TURNS", 20, [
        (1, 8, "left 90 degrees"),
        (9, 9, "left 45 degrees ahead"),
        (10, 10, "left 45 degrees behind", "(left 135 degrees)"),
        (11, 18, "right 90 degrees"),
        (19, 19, "right 45 degrees ahead"),
        (20, 20, "right 45 degrees behind", "(right 135 degrees)"),
        ]]
    ["V.chamber", "CHAMBERS", 20, [
        # table contents
    ]]
]  # END OF THE TABLE OF TABLES AKA APPENDIC A
