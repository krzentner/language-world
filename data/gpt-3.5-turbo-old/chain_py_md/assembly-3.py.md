# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put the gripper roughly above the wrench
    #  2. Line up the gripper with the opening in the wrench
    #  3. Grab the wrench
    #  4. Put the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    # If the gripper is above the wrench, line it up with the opening in the wrench.
    if check("the robot's gripper is above the wrench and the opening of the wrench is not vertical aligned with the robot's gripper"):
        robot.put("gripper in front of the opening of the wrench")
    # If the gripper is in front of the opening of the wrench, grab the wrench.
    if check("the robot's gripper is in front of the opening of the wrench and the robot's gripper is not around the wrench"):
        robot.grab("the wrench")
    # If the gripper is around the wrench and the peg is to the left of the gripper, position the wrench around the peg.
    if check("the robot's gripper is around the wrench and the peg is not to the right of the gripper"):
        robot.move("the wrench to the right of the peg")