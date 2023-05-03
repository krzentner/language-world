# peg-unplug-side: grab the peg and pull it out from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the peg is not almost left of the robot's gripper and the peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg's side and the peg is not almost horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("the peg is almost horizontally aligned with hole"):
        robot.pull("peg out of hole")