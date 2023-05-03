
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Move gripper under wall
    #  4. Move gripper to target location
    # Put gripper above the puck so that it doesn't get bumped when moving it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.move_gripper("under the wall")
    # If the gripper is under the wall, move it to the target location.
    if check("the robot's gripper is in front of the wall"):
        robot.move_gripper("near the target location")