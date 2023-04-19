# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Grab the stick with the gripper
    #  3. Put the stick roughly above the thermos
    #  4. Push the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper is not around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is around the stick and above the thermos, push the thermos
    if check("the robot's gripper is around the stick and the stick is above the thermos"):
        robot.move_gripper("above the target location")