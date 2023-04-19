

The goal is to get the thermos to the target location.

Steps:
1. Put gripper near the top of the stick
2. Drop gripper around the stick
3. Move the stick forward so it pushes the thermos to the target

# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put gripper near the top of the stick
    #  2. Drop gripper around the stick
    #  3. Move the stick forward so it pushes the thermos to the target
    # First, put the gripper near the top of the stick.
    if check("the robot's gripper is not near the top of the stick"):
        robot.move_gripper("near the top of the stick")
    # If the gripper is near the top of the stick but not around it, put it
    # around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is near the top of the stick"):
        robot.move_gripper("around the stick", close_gripper=True)
    # If the gripper is around the stick we can move it forward to push the
    # thermos to the target.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("near the target location")