# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper around the dial handle
    #  2. Turn the handle in the correct direction
    # First, put the gripper around the dial handle.
    if check("the robot's gripper is not around the dial handle"):
        robot.move_gripper("around the dial handle")
    # Determine the direction to turn the handle based on the current position.
    # If the handle is pointing down, turn it to the left.
    if check("the handle is pointing down"):
        robot.move_gripper("left of the dial handle")
    # If the handle is pointing right, turn it up.
    elif check("the handle is pointing right"):
        robot.move_gripper("above the dial handle")
    # If the handle is pointing up, turn it to the right.
    elif check("the handle is pointing up"):
        robot.move_gripper("right of the dial handle")
    # If the handle is pointing left, turn it down.
    elif check("the handle is pointing left"):
        robot.move_gripper("below the dial handle")
    # Keep turning until the lock is fully unlocked.
    if check("the lock is still locked"):
        robot.move_gripper("around the dial handle")