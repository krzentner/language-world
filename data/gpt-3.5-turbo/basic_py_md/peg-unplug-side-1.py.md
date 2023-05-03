# peg-unplug-side: grab the peg and pull it out from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the peg is not right of the robot's gripper and the peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with the hole"):
        robot.align("peg to hole vertically")
    if check("the peg is vertically aligned with the hole and the peg is not horizontally aligned with the hole"):
        robot.align("peg to hole horizontally")
    if check("the peg is horizontally aligned with the hole"):
        robot.pull("peg out of the hole")