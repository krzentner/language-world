

# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line the the thermos up with the target location
    #  4. Pull the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the stick becomes left of the gripper, go back to putting the gripper
    # above the stick.
    # Because the stick is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("stick is not left of the robot's gripper and the robot's gripper is not forward aligned with the stick"):
        robot.move_gripper("forward aligned with the stick", close_gripper=True)
    # If the gripper is around the stick, then line up the thermos with the target
    # location.
    if check("the robot's gripper is horizontally aligned with the target location"):
        robot.move_gripper("above the stick")
    # If the thermos is lined up with the target location, then pull the thermos to
    # the target location.
    if check("the robot's gripper is forward aligned with the stick and the thermos is not horizontally aligned with target location"):
        robot.move_gripper("horizontally aligned with the target location")