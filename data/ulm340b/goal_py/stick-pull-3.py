
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick
    #  3. Pull the stick around the thermos
    #  4. Move the thermos to the goal
    # First, move the gripper to the stick.
    # Put it directly above the stick, because the stick is smaller than the
    # puck.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the gripper is above the stick, we should try to grab it.
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If we've grabbed the stick, we can start moving it to pull the thermos to
    # the target location.
    if check("the robot's gripper is above the stick and the robot's gripper is closed"):
        robot.move_gripper("above the stick")

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick
    #  3. Move the stick in front of the thermos
    #  4. Push the stick into the thermos
    #  5. Move the thermos to the goal
    # First, move the gripper to the stick.
    # Put it directly above the stick, because the stick is smaller than the
    # puck.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the gripper is above the stick, we should try to grab it.
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the robot's gripper is above the stick, it may be holding the stick,
    # but we don't know for sure.
    # So, start to move the stick in front of the