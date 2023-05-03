# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put the wrench next to the peg
    #  4. Adjust the wrench to fit around the peg
    #  5. Move the wrench with the peg to the goal location
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the gripper is not around the wrench, grab the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    # If the gripper is near the wrench and open, we can probably grab it.
    if check("the robot's gripper is near wrench and the robot's gripper is open"):
        robot.close("gripper around wrench")
    # Once we have the wrench, move it next to the peg.
    if check("the robot's gripper is around wrench"):
        robot.put("wrench next to peg")
    # If the wrench is not above peg, move it above the peg.
    if check("the wrench is not vertically aligned with peg"):
        robot.move("gripper to above peg")
    # Once the wrench above the peg, adjust its position to fit around the peg.
    if check("the wrench is above the peg and the wrench does not fit around the peg"):
        robot.adjust("wrench around peg")
    # Once the wrench is around the peg, move them together to the goal.
    if check("the wrench fits around the peg"):
        robot.move("wrench with peg to goal")