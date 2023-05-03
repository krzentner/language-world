# Steps:
    #  1. Align gripper with the cube from above
    #  2. Grab the cube with the gripper
    #  3. Move the gripper and cube to the side while staying close to the ground
    #  4. Move the gripper towards the target location while staying close to the ground
    # First, we need to align the gripper with the cube from above.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # Once the gripper is aligned with the cube, we can grab it.
    if check("the robot's gripper is vertically aligned with the cube and the gripper is not around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Once the gripper is around the cube, we can move it to the side while staying close to the ground.
    if check("the robot's gripper is around the cube and the gripper is not near the target location"):
        robot.move_gripper("to the side of the current location")
    # Once the gripper and cube are to the side, we can move the gripper towards the target location while staying close to the ground.
    if check("the robot's gripper is near the target location and the gripper is around the cube"):
        robot.move_gripper("above the target location")