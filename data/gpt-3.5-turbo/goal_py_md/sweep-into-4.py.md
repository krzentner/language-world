# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the gripper to the target location, keeping the cube in the gripper and sweeping any objects in the way out of the path
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("around the cube", close_gripper=True)
    # If the gripper is around the cube and the cube is in front of the gripper, we can
    # move the gripper to the target location while sweeping any objects in the way.
    target_location = "left of the table"
    if check(f"the robot's gripper is around the cube and the cube is in front of the robot's gripper and the robot's gripper is not at {target_location}"):
        sweep_path(robot, "near the cube", target_location)
        robot.move_gripper(target_location)