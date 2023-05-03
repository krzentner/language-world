# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the hole
    #  2. Move the gripper down and into the hole
    #  3. Close gripper around peg
    #  4. Lift gripper out of the hole
    #  5. Move the gripper to the target location
    # First, put the gripper roughly above the hole
    if check("the robot's gripper is not above the hole"):
        robot.place("gripper above hole")
    # If the gripper is not in the hole, move it down into the hole
    if check("the robot's gripper is not in the hole"):
        robot.move("gripper into the hole")
    # Once the gripper is in the hole, close the gripper to hold the peg
    if check("the robot's gripper is in the hole and the gripper is open"):
        robot.close("gripper around peg")
    # Lift the gripper out of the hole with the peg
    if check("the robot's gripper is holding the peg"):
        robot.lift("gripper out of the hole")
    # Move the gripper to the target location with the peg
    if check("the robot's gripper is not at the target location"):
        robot.move("gripper to target location")