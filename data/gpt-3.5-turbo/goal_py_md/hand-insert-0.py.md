# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move the gripper to the target location
    #  4. Release the puck at the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and closed, move the gripper to the
    # target location.
    if check("the robot's gripper is near the puck and closed and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # If the gripper is near the target location, release the puck.
    if check("the robot's gripper is near the target location and the robot's gripper is closed"):
        robot.move_gripper("above the target location", close_gripper=False)