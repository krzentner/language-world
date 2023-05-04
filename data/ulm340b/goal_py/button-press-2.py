
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Line up the gripper as viewed from the front
    #  3. Push the button
    # Because this isn't "topdown", we'll line up the gripper to the button from
    # the front instead of above.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("horizontally aligned with the button", close_gripper=True)
    # Now that the gripper is lined up from the front, line it up from above.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("almost vertically aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("near the button")

# pick-place-wall: pick up the puck and hold it at the target location above
# a wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Slide gripper above the wall
    #  5. Move puck to goal
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

# peg-unstack: pick up the top block and place it to the side
def peg_unstack(robot