# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around the peg
    #  3. Close gripper around peg
    #  4. Move peg up out of the hole
    #  5. Move peg to the target location
    
    # First, put the gripper above the peg in the hole.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the hole", close_gripper=False)
        robot.move_gripper("vertically aligned with the peg")
    
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    
    # If the gripper is around the peg and closed, move the peg up out of the hole.
    if check("the robot's gripper is around the peg and closed and the robot's gripper is not near the surface"):
        robot.move_gripper("near the surface")
    
    # If the gripper is near the surface, move the peg to the target location.
    if check("the robot's gripper is near the surface and the peg is not near the target location"):
        robot.move_gripper("near the target location")