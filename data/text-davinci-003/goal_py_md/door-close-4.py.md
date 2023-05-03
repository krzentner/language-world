

# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper near door handle
    #  2. Push the door closed
    # We should put the gripper near the door handle so that we can start pushing the door.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # Now that the gripper is near the door handle, we can push it closed.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("around the door handle")