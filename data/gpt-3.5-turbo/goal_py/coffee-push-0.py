# Steps:
    #  1. Put gripper above the mug handle
    #  2. Drop the gripper around the mug handle
    #  3. Lift the mug off the table
    #  4. Move the mug to the target location
    #  5. Lower the mug onto the table
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.move_gripper("vertically aligned with the mug handle")
    # Once the gripper is lined up above the mug handle, we can grab the mug by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # Once the gripper is around the mug handle, we can lift the mug off the table by moving the gripper up.
    if check("the robot's gripper is around the mug handle and the robot's gripper is not above the table"):
        robot.move_gripper("above the table")
    # Once the gripper is above the table, we can move the mug to the target location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("on top of the target location")
    # Once the mug is at the target location, we can lower it onto the table by moving the gripper down.
    if check("the mug is at the target location and the robot's gripper is not on the table"):
        robot.move_gripper("above the table")