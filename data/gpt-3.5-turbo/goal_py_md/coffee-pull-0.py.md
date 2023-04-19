# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Pull the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the mug")
    # If the mug isn't too far away, grab it with the gripper.
    if check("the robot's gripper is above the mug and the robot's gripper is not too high above the mug and the robot's gripper is not around the mug"):
        robot.move_gripper("around the mug", close_gripper=True)
    # If the gripper is around the mug, pull it to the target location.
    if check("the robot's gripper is gripping the mug"):
        robot.move_gripper("above the target location")