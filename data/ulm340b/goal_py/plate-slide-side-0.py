
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper down around the plate
    #  3. Push plate to goal
    # We need to put the gripper above the plate before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not almost vertically aligned with the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # Once the gripper is lined up above the plate, we should be able to grab
    # the plate by moving the gripper down around it.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate")
    # Once the gripper is around the plate, we can just push it to the target
    # location.
    # Close the gripper to make sure we don't lose hold of the plate.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("above the target location")

# pick-place-wall: pick up the puck and place it on the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper down around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
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
        robot.move_gripper("near the target location")