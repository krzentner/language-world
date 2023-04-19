# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    # 1. Move to the location without hitting the wall
    while check("the robot is too close to the wall"):
        robot.move_backward()
    # 2. Put gripper above the puck
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # 3. Move the gripper to the puck without colliding with the wall
    while check("the wall is in the way of the gripper"):
        robot.move_left()
    # 4. Grab the puck with the gripper
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # 5. Move the gripper to the target location without colliding with the wall
    while check("the wall is in the way of the gripper"):
        robot.move_right()
    # 6. Hold the puck at the target location
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("near the target location")