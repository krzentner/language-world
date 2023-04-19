# hand-insert: pick up the puck and move it to the target location
# def hand_insert(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck, didnot close the gripper
    #  3. Move the puck to the target location
    #  4. Release the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, move it near the puck but don't close
    # the gripper.
    if check("the robot's gripper is not around the puck"):
        robot.move_gripper("near the puck")
    # Once the gripper is around the puck, move the puck to the target location
    # by lifting the gripper and moving it to the target location.
    if check("the robot's gripper is around the puck and the robot's gripper is not near the target location"):
        robot.move_gripper("above the target location")
    # Release the puck by opening the gripper.
    if check("the robot's gripper is near the target location and the robot's gripper is closed"):
        robot.move_gripper("near the target location", close_gripper=False)