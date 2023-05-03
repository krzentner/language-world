# Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Push cube towards target location
    #  5. Open gripper to release cube
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, drop it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it. Start pushing it towards the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed and the cube is not at target location"):
        robot.push("cube towards target location")
    # We have reached the target location, so open the gripper and release the
    # cube.
    if check("the robot's gripper is above cube and the robot's gripper is closed and the cube is at target location"):
        robot.open("gripper to release cube at target location")