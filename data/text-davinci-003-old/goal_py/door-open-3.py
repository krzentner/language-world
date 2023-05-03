
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Drop gripper around the door handle
    #  3. Pull open the door
    # We need to put the gripper above the door handle before we can grab it.
    # Line up the gripper so that it is mostly above the handle and open it.
    if check("the robot's gripper is not almost vertically aligned with the door handle"):
        robot.move_gripper("almost vertically aligned with the door handle")
    # If the gripper was open, it should be around the door handle.
    # Pull the door open by pulling the door handle left.
    if check("the robot's gripper is around the door handle"):
        robot.move_gripper("horizontally aligned with the door handle")