# Steps:
    #  1. Place gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube towards target while sweeping
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper is not around the cube, move it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is around the cube and open, try grabbing the cube by
    # closing the gripper.
    if check("the robot's gripper is around the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube towards the target while sweeping.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is near cube and the robot's gripper is closed"):
        robot.sweep_move("cube towards target")