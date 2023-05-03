
    # Steps:
    #  1. Put gripper in front of cube
    #  2. Close gripper around cube
    #  3. Lift cube
    #  4. Put cube in goal bin
    # Put the gripper in front of the cube.
    if check("the robot's gripper is not forward aligned with cube"):
        robot.place("gripper in front of cube")
    # If the gripper is near the cube, try to close the gripper around it.
    if check("the robot's gripper is forward aligned with cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # If the gripper is closed on the cube, we can try to lift it.
    if check("the robot's gripper is forward aligned with cube and the robot's gripper is closed"):
        robot.lift("cube")
    # Once the cube is lifted, just drop it in the goal bin.
    if check("the robot's gripper is forward aligned with goal bin and the robot is holding the cube"):
        robot.put("cube in bin")