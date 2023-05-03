# Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Move the gripper to the side while pulling up on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle is close to the gripper, grab it with the gripper.
    if check("the robot's gripper is above the handle and the gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper has a good hold on the handle, move the gripper to the
    # side while pulling up on the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("to the side while pulling up on the handle")