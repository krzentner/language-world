
    # Steps:
    #  1. Put gripper in front of cube
    #  2. Sweep gripper across cube to lift it
    #  3. Move cube to the target location
    # We can't pick up the cube directly, but we can push lift it with our
    # gripper.
    # To do this, we first need to align the gripper with the cube.
    if check("the robot's gripper is not forward aligned with the cube"):
        robot.put("gripper in front of cube")
    # Once the gripper is lined up with the cube, sweep the gripper across the
    # cube to lift it.
    if check("the robot's gripper is forward aligned with the cube and the cube is not above the robot's gripper"):
        robot.sweep("gripper across cube")
    # Once the cube is above the gripper, move it to the target location.
    if check("the robot's gripper is forward aligned with the cube and the cube is above the robot's gripper"):
        robot.place("cube at goal")