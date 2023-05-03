# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to target location
    #  5. Release puck
    # Start by putting the gripper roughly above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Now that the gripper is above the puck, drop it around the puck.
    if check("the robot's gripper is above the puck and not around the puck"):
        robot.move_gripper("around the puck")
    # Once the gripper is around the puck, close the gripper to pick up the puck.
    if check("the robot's gripper is around the puck and open"):
        robot.move_gripper("fully closed")
    # Now that the puck is picked up, move it to the target location.
    if check("the robot's gripper is closed and not above the target location"):
        robot.move_gripper("near the target location")
    # Release the puck once it is at the target location.
    if check("the robot's gripper is near the target location and closed"):
        robot.move_gripper("fully open")