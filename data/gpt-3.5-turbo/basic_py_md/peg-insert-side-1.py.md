```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.move("gripper to the side of the hole")
    if check("the robot's gripper is beside the hole"):
        robot.move("gripper into the hole")
    if check("the robot's gripper is in the hole and holding the peg"):
        robot.pull("gripper out of the hole")