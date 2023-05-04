
    # Steps:
    #  1. Put gripper near the lid
    #  2. Grab the lid
    #  3. Close the lid
    # First, put the gripper near the lid.
    if check("the robot's gripper is not near the lid"):
        robot.move_gripper("near the lid", close_gripper=True)
    # The robot's gripper should be around the lid if the lid is in front of the
    # robot's gripper.
    if check("the robot's gripper is near the lid and the lid is forward aligned with the robot's gripper"):
        robot.move_gripper("vertically aligned with the lid")
    # Now that the robot's gripper is on the lid, close the lid.
    if check("the robot's gripper is above the lid"):
        robot.move_gripper("almost above the box")

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place_with_camera(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck"):
        robot.move_gripper("near the puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

# box-open: pick up the box lid and put it on the table
def box_open(robot):
    # Steps:
    #  1. Put gripper near the lid
    #  2. Grab the lid
    #  3. Open the