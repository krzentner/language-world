# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put the gripper near the peg
    #  4. Lower the gripper around the peg
    # Let's start by putting the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # Now that the gripper is above the wrench, let's grab it.
    if check("the robot's gripper is above the wrench and the robot's gripper is open"):
        robot.move_gripper("around the wrench")
    # Once we have the wrench, let's bring it near the peg.
    if check("the robot's gripper is around the wrench and the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg")
    # Now that the gripper is near the peg, we can align the wrench with the peg
    # by lowering the gripper around the peg.
    if check("the robot's gripper is near the peg and the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg")
    # Now that the wrench is around the peg, the task is complete.