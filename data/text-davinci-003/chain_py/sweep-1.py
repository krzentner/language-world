
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper forwards over cube
    #  3. Close gripper around cube
    #  4. Pull cube backwards
    # First, put the gripper above cube, so that the robot can grab it from the
    # top.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper isn't forwards over the cube, move the gripper over the
    # cube.
    if check("the robot's gripper is not forwards over the cube and the robot's gripper is open"):
        robot.drop("gripper forwards over cube")
    # If the gripper is forward over the cube, maybe the cube is in the gripper.
    # Close the gripper.
    if check("the robot's gripper is forwards over the cube and the robot's gripper is open"):
        robot.grab("cube")
    # Assume the cube is in the gripper. Pull the cube back towards the goal.
    if check("the gripper is closed and the cube is in the gripper"):
        robot.pull("cube back")