# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    # 1. Put gripper above the mug
    # 2. Grab the mug with the gripper
    # 3. Move the mug to the target location
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the mug")
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not around the mug"):
        robot.move_gripper("around the mug", close_gripper=True)
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the target location")