# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    # 1. Put the gripper above the peg
    # 2. Grab the peg with the gripper
    # 3. Move the gripper above the wrench
    # 4. Place the gripper around the wrench's handle
    # 5. Move the gripper downward
    # 6. Release the wrench around the peg

    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is near the peg and closed, maybe we can grab it by moving
    # the gripper above the wrench.
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.move_gripper("above the wrench")
        robot.move_gripper("around the wrench handle")
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
        robot.move_gripper("around the peg")