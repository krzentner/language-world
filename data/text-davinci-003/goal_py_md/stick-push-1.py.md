

Steps:
1. Put the gripper below the stick
2. Wrap the gripper around the stick
3. Push the stick until it is close to the thermos
4. Move the stick until the thermos is moved to the target location

Solution: 

# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put the gripper below the stick
    #  2. Wrap the gripper around the stick
    #  3. Push the stick until it is close to the thermos
    #  4. Move the stick until the thermos is moved to the target location
    # Place the robot's gripper below the stick.
    if check("the robot's gripper is not below the stick"):
        robot.move_gripper("below the stick", close_gripper=True)
    # When the gripper is below the stick, we can grab the stick by wrapping
    # the gripper around it.
    if check("the robot's gripper is below the stick and the robot's gripper is open"):
        robot.move_gripper("around the stick")
    # Push the stick until it's close to the thermos.
    if check("the stick is not close the thermos and the robot's gripper is closed"):
        robot.move_gripper("near the thermos")
    # Move the stick until the thermos is moved to the target location.
    if check("the stick is close to the thermos"):
        robot.move_gripper("above the target location")