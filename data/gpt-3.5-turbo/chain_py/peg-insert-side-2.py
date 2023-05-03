# Steps:
    #  1. Put gripper near peg
    #  2. Grab peg with gripper
    #  3. Move gripper to hole
    #  4. Angle gripper so peg is lined up with hole
    #  5. Push peg into hole
    # First, put the gripper roughly near the peg.
    if check("the robot's gripper is not near the peg"):
        robot.move("gripper near peg")
    # If the gripper is near the peg and open, try to grab the peg.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.grab("peg with gripper")
    # If the gripper is holding the peg, move the gripper towards the hole.
    if check("the robot's gripper is holding the peg and the robot's gripper is not near the hole"):
        robot.move("gripper to hole")
    # Once the gripper is near the hole, angle the gripper so that the peg is
    # lined up with the hole.
    if check("the robot's gripper is near the hole and the gripper is angled towards the hole"):
        robot.angle("gripper for peg insertion")
    # Once the gripper is angled, we can try to push the peg into the hole.
    if check("the robot's gripper is angled towards the hole"):
        robot.push("peg into hole from the side")