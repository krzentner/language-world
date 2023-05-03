

If check("the robot's gripper is not near the peg and the robot's gripper is not horizontally aligned with the peg"):
        robot.move("gripper above the peg")
    if check("the robot's gripper is horizontally aligned with the peg and the robot's gripper is not around the peg"):
        robot.drop("the gripper around the peg")
    if check("the robot's gripper is around the peg"):
        robot.pull("the wrench away from the peg")