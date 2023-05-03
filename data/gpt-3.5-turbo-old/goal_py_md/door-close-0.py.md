# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the back of the door
    #  2. Push the door closed to the target location
    # If the gripper is not near the door, move it to the door location
    if check("the robot's gripper is not near the door location"):
        robot.move_gripper("near the door location")
    # If the gripper is near the door, start pushing it closed
    if check("the robot's gripper is near the door location"):
        robot.move_gripper("around the back of the door")
    # If the gripper is around the back of the door, push the door closed
    if check("the robot's gripper is around the back of the door"):
        robot.move_gripper("horizontally aligned with the door handle")