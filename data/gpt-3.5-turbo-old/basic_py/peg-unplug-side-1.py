if check("the robot's gripper is not vertically aligned with the peg and the gripper is not around the peg"):
        robot.put("gripper above peg")
    if check("the gripper is around the peg"):
        robot.pull("peg to the side")
    if check("the gripper is near the hole"):
        robot.align("gripper to the hole")
    if check("the gripper is above the peg and aligned with the hole"):
        robot.pull("peg out of the hole")