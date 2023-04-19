
    # Steps:
    #  1. Put gripper above wrench
    #  2. Drop wrench onto the peg
    #  3. Push wrench around peg
    #  4. Close wrench around peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # Once the gripper is above the wrench, we can drop it onto the peg.
    if check("the robot's gripper is above the wrench and the robot's gripper is not around the peg"):
        robot.drop("wrench onto peg")
    # Now that the wrench is around the peg, we can push it around the peg until
    # it is completely around it.
    if check("the robot's gripper is around the peg and the wrench is not completely around the peg"):
        robot.push("wrench around peg")
    # Once the wrench is around the peg, close it to keep it in place.
    if check("the wrench is completely around the peg"):
        robot.close("wrench around peg")