# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal

    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")

    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)

    # If the gripper is near the puck and closed, hold it in the position above the target location.
    if check("the robot's gripper is around the puck and the robot is not holding it above the target location"):
        robot.move_gripper("above the target location", close_gripper=True)