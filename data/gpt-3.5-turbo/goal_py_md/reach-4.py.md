# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Move the gripper above the target location
    #  2. Open the gripper and try to grab any objects
    #  3. If an object is grabbed, move it to a safe position
    #  4. Move the gripper down to the target location
    #  5. Close the gripper to grab any objects at the target location
    # First, move the gripper above the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # If the gripper is above any objects, try to grab them by opening the
    # gripper and moving the gripper down.
    if check("the robot's gripper is above an object"):
        robot.move_gripper("near the object", close_gripper=False)
        if check("the robot's gripper is around object"):
            robot.move_gripper("above the safe position")
    # Once we're sure there are no objects in the way, move the gripper down to
    # the target location.
    if check("the robot's gripper is not vertically aligned with the target location"):
        robot.move_gripper("vertically aligned with the target location")
    # Finally, close the gripper to grab any objects at the target location.
    if check("there is an object at the target location"):
        robot.move_gripper("around the object")