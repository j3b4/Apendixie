"""
Directions module allows for the use of relative directions by the character
and possibly other commands.  This allows you to specify "forward", "back",
"left" and "right" as commands which will determine the characters orientation,
then look for an exit that matches the relative direction.

Ex:
    If the character is facing North. Then the command "right" should move them
    East, the command "back" should move them south. If of course there is an
    exit available in the direction sought.
"""

FIXED_DIRS = [
    ('n', 'north', 0),
    ('ne', 'northeast', 45),
    ('e', 'east', 90),
    ('se', 'southeast', 135),
    ('s', 'south', 180),
    ('sw', 'southwest', 225),
    ('w', 'west', 270),
    ('nw', 'northwest', 315),
    ]

RELATIVE_DIRS = [
    ('f', 'forward', 0),
    ('fr', 'forward right', 45),
    ('r', 'right', 90),
    ('br', 'back right', 135),
    ('b', 'back', 180),
    ('bl', 'back left', 225),
    ('l', 'left', 270),
    ('fl', 'forward left', 315)
    ]


def turn(face, move):
    """
    Given a staring fixed direction, move by a relative direction and return
    the new fixed direction.
    Ex:
        facing = n # North
        move = r   # right
        return = e # East
    """
    face_dex = 0
    move_dex = 0
    for i in FIXED_DIRS:
        if face in i:
            break
        face_dex += 1

    for i in RELATIVE_DIRS:
        if move in i:
            break
        move_dex += 1

    new_face_dex = (face_dex + move_dex) % 8

    new_face = FIXED_DIRS[new_face_dex][0]

    return new_face
