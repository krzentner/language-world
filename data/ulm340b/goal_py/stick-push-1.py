
    # Steps:
    #  1. Put gripper around stick
    #  2. Grab stick with gripper
    #  3. Move gripper to above thermos
    #  4. Push down to grab thermos
    # First, put the gripper above the stick, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("above the thermos", close_gripper=True)
    # If the robot has the stick, we should have already grabbed the thermos
    # while moving above it.
    # Now we just need to pull the thermos to the target location.
    if check("the robot's gripper is around the thermos"):
        robot.move_gripper("near the target location", close_gripper=True)

# stick-place: grab the stick and place it in the target location
def stick_place(robot):
    # Steps:
    #  1. Put gripper around stick
    #  2. Grab stick with gripper
    #  3. Move gripper above goal
    #  4. Drop stick in goal
    #  5. Open gripper
    # First, put the gripper above the stick, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is near the stick and open