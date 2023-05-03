# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Close gripper around stick
    #  3. Move gripper to the thermos handle
    #  4. Position the stick loop around the handle of the thermos
    #  5. Pull the thermos to the target location
    # First, put the gripper above the stick
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is around the stick, move the gripper to the thermos handle
    if check("the robot's gripper is around the stick and the robot's gripper is not near the thermos handle"):
        robot.move_gripper("near the thermos handle")
    # If the gripper is near the thermos handle, position the stick loop around the handle of the thermos
    if check("the robot's gripper is near the thermos handle and the stick loop is not around the thermos handle"):
        robot.move_gripper("around the thermos handle")
    # If the stick is around the handle, pull the thermos to the target location
    if check("the robot's gripper is around the thermos handle"):
        robot.move_gripper("near the target location")