# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    if check("the robot's gripper is not around the mug") and check("the gripper is above the mug"):
        robot.move_gripper("around the mug", close_gripper=True)
    if check("the robot's gripper is around the mug and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")