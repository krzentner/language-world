
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Push cube towards target
    # First, we need to move the gripper roughly above the cube.
    if check("the robot's gripper is not above cube"):
        robot.move_gripper("above cube")
    # Once the gripper is above the cube, drop it down around it.
    if check("the robot's gripper is vertically aligned with cube and the robot's gripper is not around cube"):
        robot.move_gripper("around cube", close_gripper=True)
    # If the cube is now held by the gripper, push it to the target location.
    if check("the robot's gripper is closed and the robot's gripper is around cube"):
        robot.move_gripper("near the target location")