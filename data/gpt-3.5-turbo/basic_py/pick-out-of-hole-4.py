if check("the peg is not in the gripper and the gripper is not above the hole"):
        robot.move("gripper above the hole")
    if check("the peg is in the hole and the gripper is not around the peg"):
        robot.grab("the peg")
    if check("the gripper is around the peg and the peg is not at the target location"):
        robot.move("peg to target location")
    if check("the gripper is at the target location with the peg"):
        robot.drop("the peg at the target location")