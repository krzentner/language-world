# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line the stick up with the thermos handle
    #  4. Grab the thermos handle with the stick
    #  5. Pull the thermos to the target location
    # First, put the gripper roughly above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # Once the gripper is around the stick, we need to line it up with the thermos handle.
    if check("the robot's gripper is around the stick and the stick is not aligned with thermos handle"):
        robot.move_gripper("horizontally aligned with the thermos handle")
    # Once the stick is lined up with the thermos handle, we can use it to grab the handle.
    if check("the robot's gripper is around the stick and the stick is aligned with thermos handle"):
        robot.move_gripper("around the thermos handle", close_gripper=True)
    # Finally, we can pull the thermos to the target location with the stick.
    if check("the robot's gripper is around the thermos handle"):
        robot.move_gripper("near the target location")