
    if check("the robot's gripper is not horizontally aligned with the peg and the robot's gripper is not near the peg"):
        robot.put("the gripper near the peg")
    if check("the peg is not forward aligned with the robot's gripper"):
        robot.align("the peg to the gripper")
    if check("the pegr is in front of the robot's gripper and the robot's gripper is open"):
        robot.pick("the peg with the gripper")
    if check("the peg is in the robot's gripper and the robot's gripper is closed"):
        robot.place("the peg at the target")