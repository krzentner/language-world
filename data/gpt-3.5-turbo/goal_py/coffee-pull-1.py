# Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Move gripper and mug to target location
    # To start, put the gripper directly above the mug handle.
    if check("the robot's gripper is not directly above the mug handle"):
        robot.move_gripper("above the mug handle")
    # Once the gripper is above the mug handle, drop it around the handle by
    # closing the gripper.
    if check("the robot's gripper is directly above the mug handle and the robot's gripper is open"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # Once the gripper is around the mug handle, we can move the gripper and
    # mug to the target location.
    if check("the robot's gripper is around the mug handle"):
        robot.move_gripper("near the target location")