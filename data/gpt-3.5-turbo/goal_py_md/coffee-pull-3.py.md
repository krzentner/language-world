# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put the gripper around the handle of the mug
    #  2. Lift the mug
    #  3. Move the mug to the target location
    #  4. Lower the mug onto the target location
    # Begin by moving the gripper above the mug handle.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle")
    # Once the gripper is correctly positioned above the mug handle, close it
    # around the handle.
    if check("the robot's gripper is above the mug handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # With the handle securely grasped, lift the mug.
    if check("the robot's gripper is around the handle and the mug is not lifted"):
        robot.move_gripper("above the target location")
    # Move the gripper and mug to the target location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("on top of the target location", close_gripper=True)