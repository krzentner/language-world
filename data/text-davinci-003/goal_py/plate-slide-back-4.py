
    # Steps:
    #  1. Put gripper to the left of the plate
    #  2. Push the plate left
    #  3. Slide the plate to the goal
    # Because the plate is large, we don't need to be precise on the left side.
    # So, just move the gripper to the left side of the plate and start pushing.
    if check("the robot's gripper is right of the plate"):
        robot.move_gripper("left of the plate")
    # If the robot's gripper is left of the plate, start pushing it. It's ok if
    # the gripper wobbles a bit.
    if check("the robot's gripper is almost vertically aligned with the plate"):
        robot.move_gripper("horizontally aligned with the plate")
    # If the plate is still wobbling, push harder.
    if check("the robot's gripper is in front of the plate and the plate is not left of the robot's gripper"):
        robot.move_gripper("near the target location")


# pick-tableware: pick up the plate
def pick_tableware(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Lift up the plate
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Then, grab the plate by closing the gripper.
    if check("the robot's gripper is open and the robot's gripper is vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate", close_gripper=True)
    # Finally, lift up the plate by lifting the gripper upwards.
    if check("the robot's gripper is closed and the plate is in the gripper"):
        robot.move_gripper("above the plate")