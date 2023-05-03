# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put the gripper around the peg with the wrench
    #  4. Rotate the wrench to tighten it
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # If the wrench is not being grabbed already, grab it.
    if check("the robot's gripper is above the wrench and the wrench is not being grabbed"):
        robot.grab("wrench")
    # Move the gripper around the peg, making sure the wrench is wrapped around
    # the peg as well.
    if check("the robot's gripper is holding the wrench and the wrench is not wrapped around the peg"):
        robot.wrap("wrench around peg")
    # If the wrench is wrapped around the peg, rotate the wrench to tighten it.
    if check("the wrench is wrapped around the peg"):
        robot.rotate("wrench to tighten")