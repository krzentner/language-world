
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Push cube to target location
    # Put the gripper above the cube, so we don't bump it while trying to grab
    # it.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper is not around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # Once the cube is in the grip of the gripper, push it to the target
    # location.
    if check("the robot's gripper is around cube and the cube is not near goal"):
        robot.push("cube to goal")