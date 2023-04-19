
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Sweeping motion to push cube towards target
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, drop the gripper around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # Once the gripper is around the cube, do a sweeping motion to push the cube
    # towards the target.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.sweep("cube towards goal")