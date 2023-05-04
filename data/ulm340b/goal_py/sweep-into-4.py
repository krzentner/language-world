
    # Steps:
    #  1. Put gripper above the cube
    #  2. Close gripper on cube
    #  3. Sweep cube to goal
    # The robot can slide the cube by putting its gripper around the cube
    # and moving the gripper.
    # If the cube is left of the gripper and the gripper is not above the cube,
    # move the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the cube is right of the gripper, we've probably grabbed it and can
    # slide the cube to the target location.
    if check("the robot's gripper is vertically aligned with the cube and the cube is not vertically aligned with the robot's gripper"):
        robot.move_gripper("near the target location", close_gripper=True)

# sweep-into-place: pick up the cube and hold it at the target location
def sweep_into_place(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Close gripper on cube
    #  3. Move cube to goal
    # First, put the gripper roughly above cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the cube is left of the gripper and the gripper is not above the cube,
    # move the gripper above the cube.
    if check("the robot's gripper is above the cube and the cube is below the robot's gripper"):
        robot.move_gripper("almost vertically aligned with the cube", close_gripper=True)
    # If the cube is right of the gripper, we've probably grabbed it and can
    # move the cube to the target location.
    if check("the robot's gripper is above the cube and the cube is not right of the robot's gripper"):
        robot.move_gripper("vertically aligned with the target location", close_gripper=True)

# pick-into-place: pick up the object and hold it at the target location
def pick_into_