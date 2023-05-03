# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper near the handle of the mug
    #  2. Grab the handle of the mug with the gripper
    #  3. Move the mug to the target location by sliding it on the table
    # First, position the gripper near the handle of the mug.
    if check("the robot's gripper is not near the mug handle"):
        robot.move_gripper("near the mug handle")
    # Once the gripper is near the handle of the mug, grab the handle.
    if check("the robot's gripper is near the mug handle and the robot's gripper is open"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # Now that the mug is grasped by the gripper, move it to the target location.
    if check("the robot's gripper is around the mug handle"):
        robot.move_gripper("near the target location", close_gripper=True)