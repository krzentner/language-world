
    # Steps:
    #  1. Move gripper to target location
    # All we need to do is move the gripper to the target location, since there
    # is nothing to manipulate.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")

# lift: lift the object to the target location
def lift(robot):
    # Steps:
    #  1. Put gripper above object
    #  2. Grab object with gripper
    #  3. Lift object to target location
    #  4. Let go of object
    # First, put the gripper above object.
    if check("the robot's gripper is not vertically aligned with object"):
        robot.move_gripper("vertically aligned with object", close_gripper=True)
    # As long as the gripper is still above object, drop it down to grab object.
    if check("the robot's gripper is vertically aligned with object"):
        robot.move_gripper("around object")
    # As long as the robot's gripper is around object, we can lift it by moving
    # the gripper to the target location.
    if check("the robot's gripper is around object and object is not near the target location"):
        robot.move_gripper("near the target location")
    # Once the gripper is near the target location, open it to let go of the
    # object.
    if check("the robot's gripper is around object"):
        robot.move_gripper("above the target location")

# door-unlock: unlock the door by turning the key
def door_unlock(robot):
    # Steps:
    #  1. Put gripper above the key
    #  2. Grab the key with the gripper
    #  3. Unlock the door by turning the key to the right
    # First, put the gripper above the key.
    if check("the robot's gripper is not above the key"):
        robot.move_gripper("above the key", close_gripper=True)
    # If the gripper is around the key, put it below the key to pick it up.
    # The key is very long so it should be aligned with it from in front
  