# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put gripper above the peg
    #  4. Align the wrench to the peg
    #  5. Close the gripper to let the wrench wrap the peg
    
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    
    # If the gripper is above the wrench, grab it.
    if check("the robot's gripper is above the wrench and the gripper is open"):
        robot.move_gripper("around the wrench", close_gripper=True)
    
    # Once the gripper is around the wrench, put it above the peg.
    if check("the robot's gripper is around the wrench and not above the peg"):
        robot.move_gripper("above the peg")
    
    # If the gripper is above the peg, align the wrench to the peg.
    if check("the robot's gripper is above the peg and the wrench is not horizontally aligned with the peg"):
        robot.move_gripper("horizontally aligned with the peg")
    
    # Once the wrench is aligned to the peg, close the gripper to let the wrench wrap the peg.
    if check("the robot's gripper is horizontally aligned with the peg and the gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)