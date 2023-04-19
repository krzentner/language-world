
    # Steps:
    #  1. Put gripper above the hole
    #  2. Move gripper down towards the bottom of the hole
    #  3. Grab the peg with the gripper
    #  4. Move peg to goal
    # First, line up the gripper as viewed from above.
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.move_gripper("vertically aligned with the hole")
    # If the robot's gripper is above the hole, move it down towards the bottom
    # of the hole so that we can pick up the peg.
    if check("the robot's gripper is not above the hole and the robot's gripper is vertically aligned with the hole"):
        robot.move_gripper("above the hole", close_gripper=True)
    # Once we have the peg in the gripper, we can move it to the target
    # location.
    if check("the robot's gripper is above the peg and the robot gripper is closed"):
        robot.move_gripper("near the target location")