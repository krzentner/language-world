

# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Grab the stick with the gripper
    #  3. Line up the stick with the thermos 
    #  4. Push the stick to the target location
    # First, put the gripper roughly above the stick.
    if check("the robot's gripper is not nearly vertically aligned with the stick"):
        robot.move_gripper("nearly vertically aligned with the stick", close_gripper=True)
    # Now that the gripper is lined up, grab the stick.
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.move_gripper("around the stick")
    # Once the stick is grabbed, line it up with the thermos.
    if check("the robot's gripper is around the stick and the stick is not horizontally aligned with the Thermos"):
        robot.move_gripper("horizontally aligned with the Thermos")
    # If the stick and the thermos are lined up, keep the stick pointing
    # straight ahead and push it to the target location.
    if check("the stick is horizontally aligned with the Thermos"):
        robot.move_gripper("near the target location")