# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not aligned with the peg and the gripper is not open"):
        robot.grab("the peg")
    if check("the robot's gripper is aligned with peg and the gripper is open"):
        robot.close("the gripper around the peg")
    if check("the peg is not near the hole"):
        robot.move("the gripper to the side of the hole")
    if check("the peg is near the hole and the gripper is aligned with the hole"):
        robot.push("the peg into the hole")
    if check("the peg is in the hole and the gripper is holding it"):
        robot.lift("the gripper up")