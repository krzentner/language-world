
    # Steps:
    #  1. Put gripper above peg
    #  2. Line up gripper with peg from above
    #  3. Put wrench onto peg
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the peg is not left of the gripper, move the gripper above the peg
    # again.
    if check("the peg is not left of the robot's gripper and the robot's gripper is not vertically aligned with the peg"):
        robot.lineup("gripper with peg")
    # If the gripper is almost vertically aligned with the peg, we can start
    # putting the wrench on the peg.
    if check("the robot's gripper is nearly vertically aligned with the peg and the robot's gripper is still above the peg"):
        robot.put("wrench on peg")