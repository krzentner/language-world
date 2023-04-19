# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial to the right until it reaches the correct combination
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # If the dial isn't gripped by the gripper, grab it.
    # We can determine whether the gripper is gripping the dial by checking if
    # the gripper is closed and the dial is within the gripper's reach.
    if check("the robot's gripper is not gripping the dial and the robot's gripper is close to the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Once the dial is gripped, turn it to the right until it reaches the correct
    # combination.
    if check("the robot's gripper is gripping the dial and the dial is not at the correct combination"):
        robot.move_gripper("to the right of the dial") # this should turn the dial to the right
        # repeat the above step until the correct combination is reached
        while (not check("the dial is at the correct combination")):
            robot.move_gripper("to the right of the dial") 
    # Once the correct combination is reached, we're done locking the door.
    if check("the dial is at the correct combination"):
        robot.move_gripper("above the door handle") # remove gripper from dial, we're done!