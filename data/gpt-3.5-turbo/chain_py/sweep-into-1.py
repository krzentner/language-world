# Steps:
    #  1. Close gripper next to the cube
    #  2. Push gripper into the cube to sweep it up
    #  3. Move the cube to the target location
    # First, we need to position the gripper next to the cube.
    if check("the robot's gripper is not next to the cube"):
        robot.place("gripper next to cube")
    # Once the gripper is near the cube, close the gripper around it.
    if check("the robot's gripper is next to the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # Now that the gripper is around the cube, push the gripper into the cube to
    # sweep it up.
    if check("the robot's gripper is around the cube"):
        robot.push("gripper into cube")
    # The cube should now be in the gripper. Move the gripper to the target
    # location.
    if check("the robot is holding the cube and the cube is not at the target location"):
        robot.place("cube at goal")