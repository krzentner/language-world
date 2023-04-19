# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    # 1. Put gripper above hole
    # 2. Move gripper to the peg
    # 3. Grab the peg
    # 4. Move the peg up out of the hole
    # 5. Move the peg to the target location
    if check("the robot's gripper is not above the hole"):
        robot.move_gripper("above the hole")
    if check("the robot's gripper is above the hole and not around the peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    if check("the robot's gripper is around the peg and the peg is not above the hole"):
        robot.move_gripper("above the hole")
    if check("the robot's gripper is above the hole and not above the target location"):
        robot.move_gripper("above the target location")