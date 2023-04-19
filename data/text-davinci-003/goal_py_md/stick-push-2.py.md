

Then create the steps to complete the task.

# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Place the gripper on top of the stick
    #  2. Ride the stick over to the thermos
    #  3. Place the gripper near the thermos
    #  4. Push the thermos to the target location
    # First, we need to place the gripper on top of the stick so that it can be 
    # used to push the thermos.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # Now that the gripper is above the stick, move it to the thermos so that it
    # can be used to push it.
    if check("the robot's gripper is above the stick and the robot's gripper is not near the thermos"):
        robot.move_gripper("near the thermos")
    # Once the gripper is near the thermos, push it to the target location.
    if check("the robot's gripper is near the thermos"):
        robot.move_gripper("above the target location")