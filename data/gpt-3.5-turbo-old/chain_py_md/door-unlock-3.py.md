# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper on the dial
    #  2. Turn the dial to the right
    #  3. Turn the dial to the left
    #  4. Turn the dial to the right
    #  5. Pull the door open
    # First, put the gripper on the dial.
    if check("the robot's gripper is not on the dial"):
        robot.grab("dial")
    # Turn the dial to the right.
    if check("the dial is not turned to the right"):
        robot.turn("dial", "right")
    # Turn the dial to the left.
    if check("the dial is not turned to the left"):
        robot.turn("dial", "left")
    # Turn the dial to the right again.
    # The dial should now be roughly where it started, but we want to make sure
    # we're in the correct position before trying to open the door.
    if check("the dial is not turned to the right again"):
        robot.turn("dial", "right")
    # Pull the door open.
    # We might need to move the gripper to the door handle before we can open the
    # door.
    if check("the door is not open"):
        robot.put("gripper on door handle")
        robot.pull("door open")