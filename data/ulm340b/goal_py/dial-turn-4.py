
    # Steps:
    #  1. Put gripper above dial
    #  2. Grab dial from the side
    #  3. Turn dial clockwise
    # First, put the gripper above the dial so that we don't bump into it while
    # trying to grab it.
    if check("the robot's gripper is not above dial"):
        robot.move_gripper("above the dial")
    # If the gripper is vertically aligned with dial as seen from the side, we
    # can try to grab the dial.
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not around dial"):
        robot.move_gripper("around dial")
    # If the gripper is vertically aligned with dial and around it, we can try
    # to turn the dial by moving the gripper right.
    if check("the robot's gripper is around dial"):
        robot.move_gripper("vertically aligned with dial")

# pull-drawer: open the drawer to the right
def pull_drawer(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Pull the drawer open
    # First, put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the handle is horizontally aligned with the robot's gripper, try
    # pulling the drawer open.
    if check("the robot's gripper is left of the handle and the handle is horizontally aligned with the robot's gripper"):
        robot.move_gripper("right of the handle")

# push-drawer: close the drawer to the right
def push_drawer(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push the drawer close
    # First, put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the handle is left of the robot's gripper, try closing the drawer.
    if check("the handle is left of the robot's gripper"):
        robot.move_gripper("left of the handle