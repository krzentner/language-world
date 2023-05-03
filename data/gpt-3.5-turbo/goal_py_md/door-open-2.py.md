# door-open: pull the door open
def door_open(robot):
    # Steps:
    # 1. Move gripper to door handle
    # 2. Grasp door handle
    # 3. Pull the door open
    # First, move the gripper to the door handle
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # Once the gripper is near the handle, close the gripper around it.
    if check("the robot's gripper is near the door handle and the gripper is open"):
        robot.move_gripper("around the door handle", close_gripper=True)
    # Finally, pull the door open by moving the gripper horizontally away from the door handle.
    if check("the robot's gripper is around the door handle"):
        robot.move_gripper("horizontally away from the door handle")