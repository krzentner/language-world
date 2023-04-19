
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Push the cube to side of the target
    #  4. Move the cube sideways to the target
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # As long as the gripper is above the cube and the gripper isn't around the
    # cube, grab the cube.
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube"):
        robot.grab("cube")
    # As long as the cube is near the gripper, push it towards the side of the
    # target.
    if check("the cube is near the robot's gripper"):
        robot.push("cube to side of target")
    # When the cube is at the side of the target, move the cube sideways to the
    # target.
    if check("the cube is at the side of the target"):
        robot.move("cube sideways to target")