# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Drop gripper around the puck
    #  3. Close gripper around the puck
    #  4. Move the puck to the target location
    #  5. Open the gripper to release the puck

    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is not closed"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and closed, we have successfully grabbed
    # the puck. Move it to the target location.
    if check("the robot's gripper is above the puck and the robot's gripper is closed and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # Once we are at the target location, open the gripper to release the puck.
    if check("the robot's gripper is near the target location and the robot's gripper is closed"):
        robot.move_gripper("above the target location", close_gripper=False)