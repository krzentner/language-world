
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.pull("peg from hole")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.pull("peg up")
    if check("peg is above the robot's gripper and the robot's gripper is around peg"):
        robot.move("to above hole")
    if check("the robot's gripper is around peg and the peg is not vertically aligned with hole"):
        robot.align("peg to hole")
    if check("the peg is vertically aligned with the hole and the robot's gripper is around peg"):
        robot.insert("peg into hole")

# peg-unplug-topdown: grab the peg and pull the it out from above
def peg_unplug_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.pull("peg up")
    if check("peg is above the robot's gripper and the robot's gripper is around peg"):
        robot.move("to above hole")
    if check("the robot's gripper is around peg and the peg is not vertically aligned with hole"):
        robot.align("peg to hole")
  