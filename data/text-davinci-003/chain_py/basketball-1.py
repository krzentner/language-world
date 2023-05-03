
    # Steps:
    #  1. Put the gripper above the basketball
    #  2. Put down the gripper around the basketball
    #  3. Line up the basketball with the hoop
    #  4. Throw the basketball
    # First, put the gripper above the basketball.
    if check("the robot's gripper is not vertically aligned with the basketball"):
        robot.put("gripper above basketball")
    # If the gripper isn't around the basketball, put it around it.
    if check("the robot's gripper is vertically aligned with the basketball and the robot's gripper is not around the basketball"):
        robot.drop("gripper around basketball")
    # If the basketball isn't lined up with the hoop, line it up
    if check("the robot's gripper is around basketball and the basketball is not lined up with the hoop"):
        robot.align("basketball with hoop")
    # Now that the basketball is lined up with the hoop, try to throw it.
    if check("the robot's gripper is around basketball and the basketball is lined up with the hoop"):
        robot.throw("basketball into hoop")