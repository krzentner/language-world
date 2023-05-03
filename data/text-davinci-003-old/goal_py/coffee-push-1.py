
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Drop gripper around the mug handle
    #  3. Move the mug to the target location
    # The robot needs to move the mug, so we should line up its gripper with the
    # mug handle.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.move_gripper("vertically aligned with the mug handle")
    # Once the gripper is lined up with the mug handle, we can grab it by
    # moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is not around mug handle"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # After we've grabbed the mug, we can move it to its destination.
    if check("the robot's gripper is around the mug handle"):
        robot.move_gripper("horizontally aligned with the target location")