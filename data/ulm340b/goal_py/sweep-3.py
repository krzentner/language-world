
    # Steps:
    #  1. Put gripper above cube
    #  2. Close gripper on the cube
    #  3. Drag cube sideways to the goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # Next, put the gripper around the cube to hold it
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("near the cube", close_gripper=True)
    # As long as the gripper is around the cube, we can pull the cube sideways
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("above the target location")

# pick-place-side: pick up the puck and hold it at the target location
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck sideways to goal
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

# scoop: scoop the puck up by pushing it in sideways
def scoop(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Put gripper around puck
    #  3. Close gripper on puck
    # Put