

# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Place the wrench around the peg
    #  4. Close the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    # If the wrench is left of the gripper, grab it by moving the gripper around it. 
    if check("the wrench is not left of the robot's gripper"):
        robot.grab("wrench")
    # If the gripper is forward aligned with the wrench but isn't around it, 
    # place the wrench around the peg by moving the gripper according to the 
    # shape of the peg.
    if check("the robot's gripper is forward aligned with wrench and the robot's gripper is not around wrench"):
        robot.place("wrench around peg")
    # If the wrench is around the peg, close it to secure it in place.
    if check("the robot's gripper is around wrench"):
        robot.close("wrench around peg")