# hand-insert: pick up the puck and move it to the target location
# def hand_insert(robot):
    # Steps:
    #  1. Put gripper roughly above puck, but slightly off center
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to target location
    #  5. Move gripper away from puck
    # First, put the gripper roughly above the puck, but slightly off center so
    # that we can later move the puck and still have a grip on it.
    if check("the robot's gripper is not slightly off center with the puck"):
        robot.move_gripper("slightly off center with the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is around the puck and the robot's gripper is closed"):
        robot.move_gripper("above the target location")
    # If we've grabbed the puck, move it to the target location.
    # We can move the puck by just moving the gripper directly.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("away from the puck")