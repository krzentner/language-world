
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to goal
    # First, put the gripper roughly above cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube and the cube hasn't moved yet, maybe we
    # can grab the cube by closing the gripper.
    if check("the robot's gripper is around the cube and the cube is in front of the robot's gripper"):
        robot.move_gripper("above the cube")
    # If the gripper is above the cube, we can probably just move the cube to
    # the target location.
    if check("the robot's gripper is above the cube"):
        robot.move_gripper("above the target location", open_gripper=True)

# sweep-onto: push the cube into the target location
def sweep_onto(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Close gripper on top of cube
    #  3. Slide cube to goal
    # First, put the gripper roughly above cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper is above the cube and the cube hasn't moved yet, maybe we
    # can grab the cube by closing the gripper on top of it.
    if check("the robot's gripper is above the cube and the cube is in front of the robot's gripper"):
        robot.move_gripper("above the cube", close_gripper=True)
    # If the gripper is above the cube, we can probably just move the