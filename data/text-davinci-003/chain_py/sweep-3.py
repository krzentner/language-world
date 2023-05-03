
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Slide cube to the goal
    #  5. Release cube
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # Now that the gripper is around the cube and closed, let's move the cube
    # sideways.
    if check("the robot's gripper is around cube and the robot's gripper is closed"):
        robot.slide("cube sideways to goal")
    # We've moved the cube sideways and we should be able to release it
    if check("the robot's gripper is forward aligned with goal and cube is at goal"):
        robot.open("gripper releasing cube")