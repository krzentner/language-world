# peg-unplug-side: grab the peg and pull it out from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the gripper is not around the peg and the peg is not almost horizontally aligned with the hole"):
        robot.grab("peg")
    if check("the gripper is around the peg and the peg is almost horizontally aligned with the hole"):
        robot.pull("peg out of the hole to the side")