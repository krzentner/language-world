
    # Steps:
    #  1. Put gripper above basketball
    #  2. Drop gripper behind basketball
    #  3. Slide basketball forward into hoop
    # First, put the gripper above the basketball.
    if check("the robot's gripper is not above basketball"):
        robot.put("gripper above basketball")
    # Next, drop the gripper behind the basketball.
    if check("the robot's gripper is not behind basketball and the robot's gripper is open"):
        robot.drop("gripper behind basketball")
    # After the gripper is behind the basketball, and the basketball is in front
    # of the gripper, we can slide the basketball forward into the hoop.
    if check("the robot's gripper is behind basketball and the basketball is in front of the gripper"):
        robot.slide("basketball forward into hoop")