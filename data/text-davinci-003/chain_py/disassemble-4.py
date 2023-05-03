
    # Steps
    #  1. Move gripper to above the wrench
    #  2. Rotate tool with gripper
    #  3. Pull wrench off the peg
    # Move the gripper to above the wrench, so that we can rotate the wrench with
    # the gripper.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # Rotate the wrench with the gripper to try to remove it from the peg.
    if check("the robot's gripper is above the wrench and the wrench is not rotated with the robot's gripper"):
        robot.rotate("wrench with gripper")
    # If the wrench is slightly rotated with the gripper, pull it off the peg.
    if check("the robot's gripper is above the wrench and the wrench is rotated with the robot's gripper"):
        robot.pull("wrench off peg")