# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Position the gripper near the thermos cap
    #  2. Insert the stick into the thermos handle
    #  3. Push the stick through the handle and out the other side
    #  4. Move the stick towards the robot
    #  5. Grab the stick with the gripper
    #  6. Pull the thermos towards the target location
    # Position the gripper near the thermos cap.
    if check("the robot's gripper is not near the thermos cap"):
        robot.move_gripper("near the thermos cap")
    # Insert the stick into the thermos handle.
    if check("the stick is not inserted into the thermos handle"):
        robot.move_stick("into the thermos handle")
    # Push the stick through the handle and out the other side.
    if check("the stick is not pushed through the handle"):
        robot.move_stick("through the handle")
    # Move the stick towards the robot.
    if check("the stick is not near the robot"):
        robot.move_stick("towards the robot")
    # Grab the stick with the gripper.
    if check("the robot's gripper is not around the stick"):
        robot.move_gripper("around the stick")
    # Pull the thermos towards the target location.
    if check("the thermos is not at the target location"):
        robot.move_gripper("near the target location")