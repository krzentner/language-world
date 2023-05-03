
    # Steps:
    #  1. Put the gripper above the drawer handle
    #  2. Put the gripper around the drawer handle
    #  3. Pull open the drawer
    # Firstly, put the gripper above the drawer handle.
    if check("the robot's gripper is not above the drawer handle"):
        robot.put("gripper above drawer handle")
    # If the gripper is above the drawer handle, drop it around the handle.
    if check("the robot's gripper is above the drawer handle and the robot's gripper is not around drawer handle"):
        robot.drop("gripper around drawer handle")
    # With the gripper around the drawer handle, pull the drawer open.
    if check("the robot's gripper is around the drawer handle"):
        robot.pull(" drawer open")