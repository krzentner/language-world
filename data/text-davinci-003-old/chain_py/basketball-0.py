
    # Steps:
    #  1. Put gripper above the basketball
    #  2. Drop gripper around basketball
    #  3. Line up the ball with the hoop
    #  4. Lift the ball towards the hoop
    #  5. Release ball
    # First, put the gripper above the basketball.
    if check("the robot's gripper is not above the basketball"):
        robot.put("gripper above basketball")
    # Once the gripper is mostly above the basketball, we should be able to grab
    # the basketball by moving the gripper down around it.
    if check("the robot's gripper is not around basketball and the robot's gripper is open"):
        robot.grab("around basketball")
    # Once the gripper is around the basketball, line it up with the hoop.
    if check("the basketball is not horizontally aligned with the hoop and the robot's gripper is around basketball"):
        robot.align("basketball to hoop")
    # If the basketball is lined up with the hoop, lift it towards the hoop.
    if check("the basketball is horizontally aligned with the hoop"):
        robot.lift("basketball towards hoop")
    # If the basketball is close to the hoop, release it.
    if check("the basketball is close to the hoop"):
        robot.release("basketball")