# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg and the peg is in the hole"):
        robot.rotate("peg counterclockwise until it clears the hole")
    if check("the peg is out of the hole and the robot's gripper is around the peg"):
        robot.pull("peg out to the side")