# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Drop gripper around the handle
    #  3. Pull up the handle
    # First, put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once the gripper is near the handle, we should be able to grab it by moving
    # the gripper down around it.
    if check("the robot's gripper is near the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, we can pull up the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")