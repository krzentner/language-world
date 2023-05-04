
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with gripper
    #  3. Put gripper near the target location
    #  4. Put gripper above the target location
    # We need to put the gripper above the puck before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck", close_gripper=True)
    # Now that the gripper is lined up, just grab the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.move_gripper("above the puck")
    # Now that the gripper is closed around the puck, move the gripper near the
    # target location.
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.move_gripper("near the target location")
    # Now that the gripper is near the target location, put the gripper down so
    # the puck is touching the table.
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.move_gripper("above the target location")

# pick-place-w-camera: pick up the puck using the robot's camera and hold it at
#                     the target location
def pick_place_w_camera(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with gripper
    #  3. Put gripper near the target location
    #  4. Put gripper above the target location
    # We need to put the gripper above the puck before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Now that the gripper is lined up, just grab the puck.
    if check("the robot's gripper is above the puck"):
        robot.move_gripper("near the puck")
    # Now that the gripper is closed around the puck