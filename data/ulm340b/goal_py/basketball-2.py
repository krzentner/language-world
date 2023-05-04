
    # Steps:
    #  1. Get the ball above the hoop
    #  2. Drop the ball into the hoop
    #  3. Close the gripper to drop the ball
    # Get the ball above the hoop.
    if check("the ball is not above the hoop"):
        robot.move_gripper("above the hoop")
    # If the gripper is above the hoop, let go of the ball by closing the
    # gripper.
    if check("the ball is above the hoop"):
        robot.move_gripper("vertically aligned with the hoop")

# pick-place-wall: pick up the puck and hold it at the target location
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    #  5. Let go of puck
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("above the target location")
    # If the gripper is at the target location and still closed, we're done.
    if check("the robot's gripper is not at the target location and the robot's gripper is closed"):
        robot.move_gripper("near the target location", close_gripper=False)

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place_with_camera(robot):
    # Steps:
    #  1. Put gripper above puck