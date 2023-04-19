# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper above the lever handle
    #  2. Drop gripper around lever handle
    #  3. Pull the lever upward
    # First, put the gripper mostly above the lever handle.
    if check("the robot's gripper is not almost vertically aligned with lever handle"):
        robot.move_gripper("almost vertically aligned with the lever handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the lever handle"):
        robot.move_gripper("around the lever handle")
    # Once the gripper is around the lever handle, we can pull the lever
    # upward.
    if check("the robot's gripper is around lever handle"):
        robot.move_gripper("vertically aligned with the lever handle")