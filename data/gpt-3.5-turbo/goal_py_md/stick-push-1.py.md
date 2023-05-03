# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line up the stick with the thermos
    #  4. Move the stick towards the thermos
    #  5. Push the thermos to the target location using the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.move_gripper("around the stick", close_gripper=True)
    # Next, line up the stick with the thermos.
    if check("the robot's gripper is around the stick and the stick is not horizontally aligned with thermos"):
        robot.move_gripper("horizontally aligned with the thermos")
    # Once the stick and thermos are aligned, move the stick towards the thermos.
    if check("the robot's gripper is around the stick and the stick is horizontally aligned with the thermos and the robot's gripper is not near the thermos"):
        robot.move_gripper("near the thermos")
    # Finally, push the thermos towards the target location using the stick.
    if check("the robot's gripper is around the stick and the stick is horizontally aligned with the thermos and the robot's gripper is near the thermos"):
        robot.move_gripper("near the target location")