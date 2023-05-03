# Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle
    #  3. Lift the mug off the table
    #  4. Move the mug to the target location
    # If the gripper is not above the handle, move it there.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # Once the gripper is above the handle, grab it.
    if check("the robot's gripper is above the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, lift the mug by moving the gripper up.
    if check("the robot's gripper is around the handle and the robot's gripper is not vertically aligned with target location"):
        robot.move_gripper("vertically aligned with the target location")
    # Finally, move the mug to the target location by moving the gripper there.
    if check("the robot's gripper is vertically aligned with the target location and the robot's gripper is around the handle"):
        robot.move_gripper("near the target location")