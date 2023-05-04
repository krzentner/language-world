

Your program must use the function `check` and the robot method `put`, but
not the robot methods `move`, `slide`, `align`, `insert`, `push`, `reach`, `drop`,
`close`, `open`, or `pull`.


"""


def check(description):
    "*** YOUR CODE HERE ***"
    print(f"check: {description}")
    print("check:", description.replace("is", "is not"))
    return description


def robot_put(robot, description):
    "*** YOUR CODE HERE ***"
    print(f"put: {description}")


def button_press_topdown(robot):
    """Press a button down from above, using the robot gripper."""
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top

    "*** YOUR CODE HERE ***"


def door_open(robot):
    """Open a door by grabbing the door handle and pulling the door."""
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # Because this is "topdown", we just need to line up the gripper from above.

    "*** YOUR CODE HERE ***"


def drawer_open(robot):
    """Open a drawer by grabbing the drawer handle and pulling the drawer."""
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.

    "*** YOUR CODE HERE ***"


def drawer_close(robot):
    """Push a drawer to close it."""
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).

    "*** YOUR CODE HERE ***"