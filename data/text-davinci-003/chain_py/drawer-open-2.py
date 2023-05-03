
    # Steps:
    #  1. Put gripper close to the drawer handle
    #  2. Line up the gripper with the drawer handle (as viewed from front)
    #  3. Start pulling open the drawer
    #  4. Pull the drawer open harder
    # If the robot's gripper is not vertically aligned with the drawer handle, we
    # should move the gripper near the drawer handle to start pulling.
    if check("the robot's gripper is not vertically aligned with the drawer handle"):
        robot.move("gripper close to drawer handle")
    # If the robot's gripper is close to the drawer handle, line it up from the
    # front.
    if check("the robot's gripper is close to drawer handle and the robot's gripper is not forward aligned with drawer handle"):
        robot.grab("drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # pull the drawer open.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")
    # If the robot's gripper is in front of the drawer handle, the drawer is
    # probably opened, so just pull harder to make sure it's open.
    if check("the robot's gripper is in front of drawer handle"):
        robot.pull("drawer open harder")