# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the mug")
    # If the mug is not inside the gripper, move the gripper above it and grab it.
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.move_gripper("above the mug", close_gripper=True)
    # If the mug is in the gripper, move it to the target location.
    if check("the robot's gripper is around the mug"):
        robot.move_gripper("above the target location")