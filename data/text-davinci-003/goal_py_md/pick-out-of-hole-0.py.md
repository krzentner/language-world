
    
    # Steps:
    #  1. Put gripper above the hole
    #  2. Drop gripper around the peg
    #  3. Close gripper around the peg
    #  4. Move peg to goal
    # First, put the gripper above the hole so that it can see the peg.
    if check("the robot's gripper is not above the hole"):
        robot.move_gripper("above the hole")
    # If the gripper isn't around the peg, drop it arround the peg.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg, close the gripper to grab the peg.
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.move_gripper("above the target location")