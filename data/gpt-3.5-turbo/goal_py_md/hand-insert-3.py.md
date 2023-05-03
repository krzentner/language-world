# hand-insert: pick up the object and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above the object
    #  2. Drop gripper around the object
    #  3. Close gripper around the object
    #  4. Move object to target location
    # First, put the gripper roughly above the object, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the object"):
        robot.move_gripper("above the object")
    # If the gripper isn't around the object, put it around the object.
    if check("the robot's gripper is not around the object and the robot's gripper is open"):
        robot.move_gripper("near the object", close_gripper=True)
    # If the gripper is near the object and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above object and the robot's gripper is closed"):
        robot.move_gripper("near the target location")