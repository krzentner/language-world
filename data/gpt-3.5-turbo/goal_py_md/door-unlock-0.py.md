# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper near the dial handle
    #  2. Grip the handle
    #  3. Turn it 3 times counterclockwise
    # First, put the gripper near the dial handle.
    if check("the robot's gripper is not near the dial handle"):
        robot.move_gripper("near the dial handle")
    # Once the gripper is near the dial handle, we can grip it.
    if check("the robot's gripper is near the dial handle and the robot's gripper is not around the dial handle"):
        robot.move_gripper("around the dial handle")
    # Once the gripper is around the dial handle, we can turn it 3 times counterclockwise.
    if check("the robot's gripper is around the dial handle"):
        for i in range(3):
            robot.turn_dial("counterclockwise")