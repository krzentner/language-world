

Here's a description of the `robot` object you'll work with:

```
# The object that represents the robot.
class Robot(object):

    # These are the names of the objects that are in the world.
    OBJECTS = ("door handle", "reach target", "peg", "nail", "puck", "hammer", "drawer handle", "window handle")

    # These are the possible ways that the gripper can be moved.
    MOVES = ("near the " + object + " " + location for object in OBJECTS for location in ("left of ", "right of ", "above ", "below "))
    MOVES += ("horizontally aligned with " + object for object in ("door handle", "drawer handle", "window handle", "hammer"))
    MOVES += ("vertically aligned with " + object for object in ("door handle", "drawer handle", "window handle", "hammer"))
    MOVES += ("almost vertically aligned with " + object for object in OBJECTS)
    MOVES += ("forward aligned with " + object for object in ("peg", "hammer"))
    MOVES += ("around " + object for object in OBJECTS)
    MOVES += ("not around " + object for object in OBJECTS)
    MOVES += ("near " + object for object in OBJECTS)
    MOVES += ("not near " + object for object in OBJECTS)

    # Each of these is a sentence that the robot can say to itself.
    STATEMENTS = ("the robot's gripper is " + move for move in MOVES)
    STATEMENTS += ("the " + object + " is " + move for object in OBJECTS for move in MOVES)

    # These are the commands that the robot can do.
    # (All the possible ways the robot can tell its gripper to move.)
    COMMANDS = ("near " + object + " " + location for object in OBJECTS for location in ("left of ", "right of ", "above ", "below "))
    COMMANDS += ("vertically aligned with " + object for object in ("door handle", "drawer handle", "window handle", "hammer"))
    COMMANDS += ("horizontally aligned with " + object for object in ("door handle", "drawer handle", "window handle", "hammer"))
    COMMANDS += ("almost vertically aligned with " + object for object in OBJECTS)
    COMMANDS += ("forward aligned with " + object for object in ("peg", "hammer"))
    COMMANDS += ("near " + object for object in OBJECTS)
    COMMANDS += ("left of " + object for object in OBJECTS