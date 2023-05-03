
    # Steps:
    #  1. Put gripper to the side of hole
    #  2. Control direction of force to insert peg
    #  3. Push peg into the hole
    # First we need to line up the gripper with the hole 4-5 cm away.
    if check("the robot's gripper is not in position for inserting the peg from the side"):
        robot.put("gripper to the side of the hole")
    # Now that the robot's gripper is in the right place, we can try to insert
    # the peg. We don't want to just push the peg into the hole, because that
    # won't work. We need to control the direction of the force so that the peg
    # slides in properly.
    if check("the robot's gripper is in position for inserting the peg from the side"):
        robot.control("direction of force")
    # Once we're ready to insert the peg, push it into the hole.
    # We don't want to put it in too hard to avoid damage to the hole or the peg.
    if check("the robot's gripper is pushing the peg correctly"):
        robot.push("peg into the hole")