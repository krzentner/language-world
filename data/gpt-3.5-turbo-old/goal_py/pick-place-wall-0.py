# Steps:
    # 1. Put gripper above puck
    # 2. Check if wall is in the way
    # 3. If wall is in the way, move gripper to side of wall
    # 4. Drop gripper around puck
    # 5. Close gripper around puck
    # 6. Move puck to goal
    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Check if there is a wall between the gripper and the puck keeping the gripper from reaching the puck
    if check("wall is in the way between the gripper and the puck"):
        robot.move_gripper("to the side of the wall")
    # If the gripper is not around the puck, put it around the puck
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")