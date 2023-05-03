# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate towards the target location
    # First, put the gripper roughly above the plate
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, move it around the plate.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is around the plate and not yet sliding towards the target location, slide it sideways towards the target location.
    if check("the robot's gripper is around the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")

# cup-flip: flip the cup upside-down
# def cup_flip(robot):
    # Steps:
    #  1. Put gripper above cup
    #  2. Grab the cup with the gripper
    #  3. Flip the cup upside-down
    # First, put the gripper roughly above the cup.
    if check("the robot's gripper is not above the cup"):
        robot.move_gripper("above the cup")
    # If the gripper isn't around the cup, move it around the cup.
    if check("the robot's gripper is not around the cup and the robot's gripper is open"):
        robot.move_gripper("near the cup", close_gripper=True)
    # If the gripper is around the cup and the cup is not yet flipped, flip it upside-down.
    if check("the robot's gripper is around the cup and the cup is not upside-down"):
        robot.move_gripper("around the center of the cup")