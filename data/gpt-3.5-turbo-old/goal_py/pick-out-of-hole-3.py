# Steps:
    # 1. Put gripper above the hole
    # 2. Slide the gripper down into the hole and grab the peg
    # 3. Lift the peg out of the hole
    # 4. Move the gripper to the target location with the peg
    # First, put the gripper above the hole.
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.move_gripper("vertically aligned with the hole")
    # If the gripper is above the hole but not inside, move it inside to grab
    # the peg.
    if check("the robot's gripper is above the hole and not around the peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Once the gripper is around the peg, lift it out of the hole.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("above the target location")