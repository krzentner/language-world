

Steps:
1. Put gripper above hole
2. Drop gripper around peg
3. Close gripper around peg
4. Move peg to goal

# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above hole
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move peg to goal
    # First, put the gripper above the hole in order to locate the peg.
    if check("the robot's gripper is not above the hole"):
        robot.move_gripper("above the hole")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg and open, close the gripper to hold the 
    # peg.
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.move_gripper("above the target location")