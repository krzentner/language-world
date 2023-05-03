# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper in front of the mug's handle
    #  2. Grab the mug's handle with the gripper
    #  3. Lift the mug and move it to the target location
    #  4. Lower the mug onto the target location
    # First, put the gripper in front of the mug's handle.
    if check("the robot's gripper is not in front of the mug's handle"):
        robot.move_gripper("in front of the mug's handle")
    # If the gripper isn't around the mug's handle, put it around the handle.
    if check("the robot's gripper is not around the mug's handle and the robot's gripper is open"):
        robot.move_gripper("around the mug's handle", close_gripper=True)
    # If the gripper is around the mug's handle, lift the mug and move it to
    # the target location.
    if check("the robot's gripper is around the mug's handle" and "the robot's gripper isn't near the target location"):
        # Lift the mug.
        robot.move_gripper("above the target location")
        # Move the mug to the target location.
        robot.move_gripper("near the target location")
    # If the gripper is near the target location, lower the mug onto it.
    if check("the robot's gripper is near the target location" and "the mug is above the target location"):
        robot.move_gripper("on the target location")