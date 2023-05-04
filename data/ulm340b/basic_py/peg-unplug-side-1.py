
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.unplug("peg from hole")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not forward aligned with the robot's gripper and the robot's gripper is not around the peg"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole and the robot's gripper is around peg"):
        robot.insert("peg into hole")

# peg-unplug-topdown: grab the peg and pull the it out from above
def peg_unplug_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not forward aligned with the robot's gripper and the robot's gripper is not around the peg"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole and the robot's gripper is around peg"):
        robot.unplug("peg from hole")

# hook-unhook: hook/unhook the hook
def hook_unhook(robot):
    if check("the robot's gripper is not almost vertically aligned with the hook"):
        robot.put("gripper above hook")
    if check("the robot's gripper is almost vertically aligned with the hook and the robot's gripper is not around hook"):
        robot.put("