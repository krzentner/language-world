# Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Lift box lid off
    #  5. Put gripper above box
    #  6. Drop gripper on top of box
    #  7. Open gripper to release box lid onto box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # Next, drop the gripper around the box lid and close it to grab onto the lid.
    if check("the robot's gripper is above box lid and the robot's gripper is not around box lid"):
        robot.move_gripper("around the box lid", close_gripper=True)
    # Lift the box lid off the box.
    if check("the robot's gripper is around box lid"):
        robot.move_gripper("above the box")
    # Move the gripper over the box and open it to release the box lid onto the box.
    if check("the robot's gripper is above the box and the robot's gripper is closed"):
        robot.move_gripper("on top of the box", close_gripper=False)