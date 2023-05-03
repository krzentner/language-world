
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with gripper
    #  3. Move cube 180 degrees to target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper isn't touching the cube, move the gripper down around it to
    # grab it.
    if check("the robot's gripper is not near the cube and the robot's gripper is open"):
        robot.move("gripper around cube")
    # Once the gripper is around the cube, we can move the gripper sideways
    # around the cube and into the target location.
    if check("the robot's gripper is around the cube and the robot's gripper is open"):
        robot.move("cube 180 degrees to target location")