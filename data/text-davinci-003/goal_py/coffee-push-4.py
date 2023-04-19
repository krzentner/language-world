
    # Steps:
    # 1. Put gripper above the mug
    # 2. Drop gripper around the mug
    # 3. Grab the mug with the gripper
    # 4. Pick the mug up
    # 5. Move the mug to the target location
    # First, put the gripper above the mug, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
    # If the gripper is near the mug and open, maybe we can grab it by closing the
    # gripper.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.move_gripper("upwards with the mug")
    # Once the mug is securely held in the gripper, move the mug to the target
    # location.
    if check("the robot's gripper is above the mug and the mug is above the robot's gripper")
        robot.move_gripper("above the target location")