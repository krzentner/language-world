

# basketball: put the ball into into the hoop
# def basketball(robot):
    # Steps:
    #  1. Line up the robot's gripper with the basketball
    #  2. Reach for the basketball and grip it
    #  3. Lift the basketball
    #  4. Line up the basketball with the hoop
    #  5. Shoot the basketball into the hoop
    # First, line up the robot's gripper with the basketball.
    if check("the robot's gripper is not forward aligned with the basketball"):
        robot.move_gripper("forward aligned with the basketball")
    # When the gripper is forward aligned with the basketball, grab it.
    if check("the robot's gripper is forward aligned with basketball"):
        robot.move_gripper("around the basketball", close_gripper=True)
    # Once the gripper is around the basketball, lift it up.
    if check("the robot's gripper is around the basketball"):
        robot.move_gripper("above the hoop")
    # Line up the basketball with the hoop.
    if check("the basketball is not aligned with the hoop"):
        robot.move_gripper("vertically aligned with the hoop")
    # Finally, shoot the ball into the hoop by pushing it forward.
    if check("the robot's gripper is vertically aligned with the hoop"):
        robot.move_gripper("left of the hoop", close_gripper=False)