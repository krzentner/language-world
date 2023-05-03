# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
# The robot first moves its gripper to the bin location
    if check("the robot's gripper is not near the bin location"):
        robot.reach("to bin location")
# The robot then moves its gripper to the cube location
    if check("the robot's gripper is not near the cube location"):
        robot.reach("to cube location")
# The robot then picks up the cube
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is not near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
# The robot then moves its gripper to the bin location
    if check("the robot's gripper is not near the bin location"):
        robot.reach("to bin location")
# The robot then places the cube in the bin
    if check("the robot's gripper is near the bin location and the robot's gripper is closed"):
        robot.place("the cube in the bin")