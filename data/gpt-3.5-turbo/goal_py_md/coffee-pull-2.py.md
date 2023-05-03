# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Grab the mug by its handle
    #  3. Move the mug to the target location by pulling it towards us
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.move_gripper("vertically aligned with the mug handle")
    # Once the gripper is above the mug handle, we can grab the mug by moving
    # the gripper down and closing it around the handle.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # After we have a firm grip on the mug's handle, we need to pull it towards
    # us by moving the gripper towards the target location. 
    # Make sure the mug doesn't collide with any other objects in its path.
    if check("the robot's gripper is around the mug handle"):
        robot.move_gripper("right of the mug handle")
        robot.move_gripper("forward aligned with the mug handle")
        robot.move_gripper("near the target location")