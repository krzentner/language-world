# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    # 1. Put the gripper above the wrench
    # 2. Open the gripper
    # 3. Move the gripper near the peg
    # 4. Close the gripper around the wrench
    # 5. Move the wrench to the peg
    # 6. Slide the gripper off the wrench and leave it around the peg
    
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    if check("the robot's gripper is above the wrench and the robot's gripper is not open"):
        robot.move_gripper("near the wrench", close_gripper=False)
    if check("the robot's gripper is open and the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg", close_gripper=False)
    if check("the robot's gripper is near the peg and the robot's gripper is not closed around the wrench"):
        robot.move_gripper("around the wrench", close_gripper=True)
    if check("the robot's gripper is holding the wrench and the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg")
    if check("the robot's gripper is near the peg and the wrench is above the peg"):
        robot.move_gripper("above the wrench")
    if check("the robot's gripper is above the wrench and the wrench is aligned with the peg"):
        robot.move_gripper("around the peg", close_gripper=False)