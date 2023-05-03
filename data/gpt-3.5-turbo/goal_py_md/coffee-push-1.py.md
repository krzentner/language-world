# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Move the mug to the target location by sliding it
    # Begin by putting the gripper above the mug handle.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle")
    # Once the gripper is roughly above the mug handle, we can grab the handle
    # by dropping the gripper around it and closing it.
    if check("the robot's gripper is above the mug handle and the robot's gripper is open"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # Once the gripper is around the mug handle, we can slide the mug to the
    # target location.
    if check("the robot's gripper is around the mug handle"):
        robot.move_gripper("near the target location")