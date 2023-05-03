

# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line the wrench up with the peg
    #  4. Close the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the wrench.
    if check("wrench is not left of the robot's gripper and the wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    # As long the gripper is still mostly around the wrench and the wrench isn't lined
    # up with the peg, line up the wrench with the peg.
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not horizontally aligned with the peg"):
        robot.align("wrench to peg")
    # If the wrench is lined up with the peg to the side, close it.
    if check("wrench is horizontally aligned with the peg"):
        robot.close("wrench around peg")