

# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper above door lock
    #  2. Turn the dial clockwise
    #  3. Turn the dial slightly counterclockwise
    #  4. Turn the dial counterclockwise
    # First, put the gripper roughly above door lock.
    if check("the robot's gripper is not vertically aligned with the door lock"):
        robot.move_gripper("vertically aligned with the door lock")
    # Once the gripper is above the door lock, we can start turning the dial.
    # We should start turning the dial clockwise.
    if check("the robot's gripper is not above the door lock"):
        robot.move_gripper("above the door lock", close_gripper=True)
    # Once the gripper is near the door lock, we can start rotating the dial
    # clockwise.
    if check("the robot's gripper is near the door lock and the robot's gripper is vertical aligned with the door lock"):
        robot.move_gripper("right of the door lock")
    # Once the gripper is certain distance away and facing the door lock, we can
    # turn the dial counterclockwise slightly before turning it counterclockwise
    # to complete the turn.
    if check("the robot's gripper is facing the door lock"):
        robot.move_gripper("left of the door lock")