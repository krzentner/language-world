

The steps for the stick-push task are as follows:

1. Put gripper above the stick
2. Drop gripper around the stick
3. Slide the stick to the target location

# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Drop gripper around the stick
    #  3. Slide the stick to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the stick is aligned with the gripper as seen from in front, we can
    # slide the stick to the target location.
    if check("the robot's gripper is forward aligned with stick"):
        robot.move_gripper("around the stick")
    #Once the stick is lined up, slide it to the target location.
    if check("the robot's gripper is around stick"):
        robot.move_gripper("near the target location")