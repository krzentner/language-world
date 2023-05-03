# Steps:
    #  1. Put gripper above wrench
    #  2. Grab wrench with gripper
    #  3. Twist gripper to loosen wrench from peg
    #  4. Lift gripper to remove wrench from peg
    # First, position the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # If the gripper isn't around the wrench, grab it.
    if check("the robot's gripper is not around wrench"):
        robot.grab("wrench")
    # Once the wrench is grabbed, we can twist the gripper slightly to loosen
    # the wrench from the peg.
    if check("the wrench is grabbed by the gripper"):
        robot.twist("gripper to loosen wrench")
    # Once the wrench is loosened, we can lift the gripper to remove the wrench
    # from the peg.
    if check("the wrench is mostly lifted from the peg"):
        robot.lift("wrench from peg")