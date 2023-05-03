
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around the peg
    #  3. Push gripper down
    #  4. Pull peg out of hole
    #  5. Move peg to goal
    # Put the gripper near the peg and push it down to start pulling it out.
    if check("the robot's gripper is not between the peg and hole"):
        robot.move_gripper("between the peg and hole")
    # If the gripper is in the right spot but isn't holding the peg yet, close
    # the gripper.
    if check("the robot's gripper is between the peg and hole and the gripper is not closed"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is too close to the peg, we may not have it secured. Move
    # it back up a little bit and try again.
    if check("the robot's gripper is not between the peg and hole and the robot's gripper is closed"):
        robot.move_gripper("above the peg")
    # Once the peg is secured, move it to the target location.
    if check("the robot's gripper is between the peg and hole and the robot's gripper is closed"):
        robot.move_gripper("near the target location")