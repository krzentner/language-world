# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above hole
    #  2. Move gripper down to visually locate peg
    #  3. Move gripper above peg
    #  4. Grab the peg with the gripper
    #  5. Line the peg up with the target location
    #  6. Move the peg to the target location
    #  7. Hold the peg at the target location
 
    # First, put the gripper roughly above the hole.
    if check("the robot's gripper is not roughly above the hole"):
      robot.move_gripper("roughly above the hole")
 
    # Move the gripper down slowly until it locates the peg and almost touches it.
    if check("the robot's gripper is not almost touching the peg"):
        robot.move_gripper("almost touching the peg")
 
    # Move the gripper above the peg and grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg", close_gripper=True)
 
    # Line up the peg with the target location.
    if check("the peg is not near the target location"):
        robot.move_gripper("near the target location")
 
    # Move the peg to the target location.
    if check("the peg is not at the target location"):
        robot.move_gripper("at the target location")
 
    # Hold the peg at the target location.
    if check("the peg is not being held at the target location"):
        robot.move_gripper("hold the peg")