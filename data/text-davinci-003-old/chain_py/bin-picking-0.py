
    # Steps:
    #  1. Reach towards the cube
    #  2. Put gripper above cube
    #  3. Drop gripper around cube
    #  4. Close gripper around cube
    #  5. Move cube towards bin
    #  6. Drop cube in bin
    # First, we need to move the robot's gripper close to the cube.
    if check("the robot's gripper is not near cube"):
        robot.reach("towards cube")
    # Once the gripper is close, try to grab it.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper is in the correct position, try to grab the cube by
    # moving the gripper around it.
    if check("the robot's gripper is above cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # Once the gripper is around the cube and the gripper is open, just close
    # it and the cube should be trapped.
    if check("the robot's gripper is above cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # If the cube is trapped, move it to the bin.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move("cube towards bin")
    # If the cube is close to the bin, just drop it in.
    if check("the cube is close to bin"):
        robot.drop("cube in bin")