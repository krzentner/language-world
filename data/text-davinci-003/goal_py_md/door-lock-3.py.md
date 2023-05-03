

This task requires the robot to rotate a dial to a certain position. 

# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put the gripper above the dial
    #  2. Drop the gripper around the dial
    #  3. Slowly rotate the dial to the desired position
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.move_gripper("vertically aligned with the dial")
    # Next, drop the gripper around the dial.
    if check("the robot's gripper is vertically aligned with dialog and the robot's gripper is not around dial"):
        robot.move_gripper("around the dial")
    # Lastly, slowly rotate the dial to the desired position.
    if check("the robot's gripper is around the dial"):
        robot.rotate_gripper("counter clockwise")