# Steps:
    #  1. Put gripper left of the peg
    #  2. Move gripper towards the peg
    #  3. Grab the peg
    #  4. Move gripper towards the hole
    #  5. Insert the peg into the hole
    # First, put the gripper to the left of the peg.
    if check("the robot's gripper is not left of the peg and the robot's gripper is not vertically aligned with the peg"):
        robot.move("gripper to left of peg")
    # Once the gripper is left of the peg, move it towards the peg.
    if check("the robot's gripper is left of the peg and the robot's gripper is not near the peg"):
        robot.move("gripper towards peg")
    # Once the gripper is near the peg, grab it.
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.grab("peg")
    # Once the gripper has grabbed the peg, move it towards the hole.
    if check("the robot's gripper is holding the peg and the robot's gripper is not near the hole"):
        robot.move("gripper towards hole")
    # Once the gripper is near the hole, insert the peg into the hole.
    if check("the robot's gripper is holding the peg and the robot's gripper is in front of the hole"):
        robot.insert("peg into hole from the side")