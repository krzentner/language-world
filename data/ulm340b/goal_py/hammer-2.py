
    # Steps:
    #  1. Line up the hammer as viewed from above
    #  2. Push down on the nail
    #  3. Pull the hammer back
    #  4. Go to step 2
    # First, line up the hammer as viewed from above.
    if check("the hammer is not vertically aligned with nail"):
        robot.move_gripper("vertically aligned with nail", close_gripper=True)
    # Now that the hammer is aligned, we can hit the nail!
    # Once the hammer has dropped, pull it back up.
    if check("the hammer is vertically aligned with nail"):
        robot.move_gripper("near nail")

# lift: lift the box in the air using the robot's gripper
def lift(robot):
    # Steps:
    #  1. Put gripper above box
    #  2. Drop gripper around box
    #  3. Close gripper around box
    #  4. Lift box in air
    # First, put the gripper roughly above box, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the box"):
        robot.move_gripper("vertically aligned with box", close_gripper=True)
    # Once the gripper is near the box, we can close it around the box.
    if check("the robot's gripper is vertically aligned with box"):
        robot.move_gripper("near the box")
    # Once the gripper is near the box and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is not around box"):
        robot.move_gripper("vertically aligned with box")
    # Once the box is picked up, lift it in the air.
    if check("the robot's gripper is below the box"):
        robot.move_gripper("above the box")

# pour: pour from one cup into the other
def pour(robot):
    # Steps:
    #  1. Put gripper above the blue cup
    #  2. Grab the blue cup
    #  3. Line up the blue cup with the green cup
    #  4. Pour blue cup into