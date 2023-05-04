
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Move cube to goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # If the gripper is around the cube, we can move it to the goal.
    if check("the robot's gripper is above the cube"):
        robot.move_gripper("around the target location")

# sweep-onto: grab the cube and move it to the target location
def sweep_onto(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Move cube to goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # If the gripper is around the cube, we can move it to the goal.
    if check("the robot's gripper is above the cube"):
        robot.move_gripper("around the target location")

# tap: move the gripper until it touches the object
def tap(robot):
    # Steps:
    #  1. Put gripper above object
    #  2. Move gripper closer to object
    #  3. Move gripper towards object until it touches
    # First, we move the gripper so that it's above the object we want to tap.
    if check("the robot's gripper is not above object"):
        robot.move_gripper("above object", close_gripper=True)
    # When the gripper