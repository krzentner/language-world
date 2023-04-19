# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with gripper
    #  3. Move the mug to the target location
    # First, put the gripper roughly above the mug, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
    # Once the gripper is around the mug, we can move it to the target location.
    if check("the robot's gripper is around the mug"):
        robot.move_gripper("near the target location")