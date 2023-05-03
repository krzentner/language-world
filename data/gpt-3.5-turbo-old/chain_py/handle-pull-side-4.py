# Steps:
    #  1. Put gripper roughly above handle
    #  2. Move gripper to side of handle
    #  3. Grab handle with gripper
    #  4. Pull handle up
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move("gripper above handle")
    # Next, move the gripper to the side of the handle.
    if check("the robot's gripper is not to the side of the handle"):
        robot.move("gripper to the side of handle")
    # If the gripper is correctly positioned, we can now grab the handle.
    if check("the robot's gripper is next to handle and the robot's gripper is open"):
        robot.grab("handle")
    # Once the gripper is holding the handle, we can pull it up.
    if check("the robot's gripper is holding the handle"):
        robot.pull("up on handle")