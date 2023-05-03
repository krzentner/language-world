# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Lift the mug and move it to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the mug")
    # If the gripper isn't around the mug, move it down to the mug to grip it.
    if check("the robot's gripper is above the mug and the robot's gripper is not around mug"):
        robot.move_gripper("around the mug", close_gripper=True)
    # If the gripper has the mug gripped, lift the mug.
    if check("the robot's gripper is around the mug"):
        robot.move_gripper("near the target location", enable_lift=True)
    # Once above the target location, place the mug.
    if check("the robot's gripper is near the target location and the robot's gripper is lifted"):
        robot.move_gripper("near the target location", enable_lift=False)