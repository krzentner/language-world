# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put the gripper above the wrench
    #  2. Move the gripper to an opening in the wrench
    #  3. Close the gripper around the wrench opening
    #  4. Lift the wrench and move it towards the peg
    #  5. Put the gripper above the peg
    #  6. Move the gripper down around the peg
    #  7. Open the gripper to release the wrench around the peg
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    if check("the robot's gripper is above the wrench and the gripper is not in an opening in the wrench"):
        robot.move_gripper("in an opening in the wrench", close_gripper=True)
    if check("the gripper is in an opening in the wrench and the gripper is open"):
        robot.move_gripper("above the peg", close_gripper=True)
    if check("the robot's gripper is above the peg and the gripper is closed"):
        robot.move_gripper("around the peg")
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("above the peg", close_gripper=False)