# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #   1. Put gripper above the mug handle
    #   2. Drop gripper around the mug handle
    #   3. Close the gripper around the mug handle
    #   4. Pull the mug to the target location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle")
    # Once above the mug handle, drop the gripper around it.
    if check("the robot's gripper is not around the mug handle and the robot's gripper is above the mug handle"):
        robot.move_gripper("near the mug handle", close_gripper=True)
    # Grip the mug handle.
    if check("the robot's gripper is around mug handle"):
        robot.move_gripper("around the mug handle")
    # Now that the gripper is around the mug handle, move it to the target location.
    if check("the robot's gripper is around mug handle"):
        robot.move_gripper("near the target location")