# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    # 1. Place gripper above the handle of the mug
    # 2. Close the gripper around the handle
    # 3. Move the gripper to the target location while keeping a firm grip on the mug.
    if check("the robot's gripper is not above the handle of the mug"):
        robot.move_gripper("above the handle of the mug")
    if check("the robot's gripper is above the handle of the mug and the robot's gripper is open"):
        robot.move_gripper("around the handle of the mug", close_gripper=True)
    if check("the robot's gripper is around the handle of the mug and the robot's gripper is not at the target location"):
        robot.move_gripper("near the target location")