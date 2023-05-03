# peg-insert-side: insert the peg into the hole from the side
# def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the gripper is above the peg, grab the peg with the gripper.
    if check("the robot's gripper is above the peg and the robot's gripper is open"):
        robot.grab("peg")
    # Once the gripper is around the peg, align the peg with the hole by moving
    # it horizontally and vertically.
    # We'll start by moving horizontally.
    if check("the robot's gripper is around peg and the peg is not horizontally aligned with the hole"):
        robot.move("peg horizontally to hole")
    # If the peg is horizontally aligned with the hole, we can align it
    # vertically by moving it down.
    if check("peg is horizontally aligned with hole and the peg is not vertically aligned with the hole"):
        robot.move("peg vertically to hole")
    # If the peg is aligned with the hole in both directions, insert it by
    # sliding it.
    if check("peg is aligned with hole"):
        robot.insert("peg into hole")