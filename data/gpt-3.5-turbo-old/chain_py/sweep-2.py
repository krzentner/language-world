# Steps:
    #  1. Put gripper above cube
    #  2. Grab the cube with the gripper
    #  3. Tilt the gripper so that one side is on the ground
    #  4. Slide the cube to the target location while keeping one side of the
    #     gripper on the ground
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # Grab the cube with the gripper.
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.grab("cube")
    # Tilt the gripper so that one side is on the ground.
    if check("the robot's gripper is properly aligned with the cube and the robot's gripper needs to be tilted"):
        robot.tilt("gripper to the side")
    # Slide the cube to the target location while keeping one side of the gripper
    # on the ground.
    if check("the robot's gripper is tilted and the cube is in contact with the ground"):
        robot.slide("cube to goal")