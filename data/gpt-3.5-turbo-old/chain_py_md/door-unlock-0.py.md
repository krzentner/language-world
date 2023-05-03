# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Move gripper to the dial handle
    #  2. Grab the handle with the gripper
    #  3. Turn the handle to the right
    #  4. Stop turning when the handle clicks
    # First, move the gripper to the dial handle.
    if check("the robot's gripper is not near the dial handle"):
        robot.move("gripper to the dial handle")
    # If the gripper is near the handle and the gripper is open, close it to
    # grab the handle.
    if check("the robot's gripper is near the dial handle and the robot's gripper is open"):
        robot.grab("the dial handle")
    # Once the handle is grabbed, turn it slowly to the right.
    # We don't want to apply too much force or overshoot the correct position.
    if check("the robot's gripper is holding the dial handle"):
        robot.turn("the dial to the right slowly")
    # Listen for the audible click that indicates the correct combination has been entered.
    if check("the robot's gripper is holding the dial handle and the lock has clicked"):
        robot.stop("turning the dial")