# Steps:
    #  1. Put gripper near peg
    #  2. Drop gripper around peg
    #  3. Move gripper and peg to the hole
    #  4. Insert peg into the hole
    # First, put the gripper near the peg.
    if check("the robot's gripper is not near the peg"):
        robot.move("gripper near peg")
    # Once the gripper is near the peg, we need to drop it around the peg so we
    # can pick it up and move it to the hole.
    if check("the robot's gripper is near peg and the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    # If the gripper is around the peg, we should have control of it. Move it
    # over to the hole.
    if check("the robot's gripper is around peg and the peg is not near the hole"):
        robot.move("gripper and peg to hole")
    # If the gripper and peg are near the hole, try to insert the peg.
    if check("the robot's gripper and peg are near the hole"):
        robot.push("peg into hole")