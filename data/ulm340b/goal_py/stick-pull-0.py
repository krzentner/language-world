
    # Steps:
    #  1. Put gripper near the stick
    #  2. Grab the stick with the gripper
    #  3. Pull the stick to the left
    # If the gripper is not near the stick, move the gripper to the stick.
    # Because the stick is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is not forward aligned with the stick"):
        robot.move_gripper("forward aligned with the stick")
    # If the gripper is lined up with the stick and the stick isn't behind the
    # gripper, we can try to grab the stick.
    if check("the robot's gripper is aligned with the stick and the robot's gripper is forward aligned with the stick"):
        robot.move_gripper("above the stick", close_gripper=True)
    # If the stick is behind the gripper we can pull it.
    if check("the robot's gripper is behind the stick"):
        robot.move_gripper("left of the stick", open_gripper=True)

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper near the stick
    #  2. Grab the stick with the gripper
    #  3. Push the stick to the right
    # If the gripper is not near the stick, move the gripper to the stick.
    # Because the stick is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is not forward aligned with the stick"):
        robot.move_gripper("forward aligned with the stick")
    # If the gripper is lined up with the stick and the stick isn't behind the
    # gripper, we can try to grab the stick.
    if check("the robot's gripper is aligned with the stick and the robot's gripper is forward aligned with the stick"):
        robot.move_gripper("above the stick", close_gripper=True)
    # If the stick is behind the gripper we can push it.
    if check("the robot's grip