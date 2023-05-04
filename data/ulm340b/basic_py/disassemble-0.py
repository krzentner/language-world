
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is above the wrench and the robot's gripper is not around wrench"):
        robot.put("gripper around wrench")
    if check("the robot's gripper is vertically aligned with wrench and the robot's gripper is not closed around wrench"):
        robot.close("gripper around wrench")
    if check("the robot's gripper is closed around the wrench"):
        robot.pull("wrench off peg")

# peg-unplug-side: grab the peg and pull it out of the hole to the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is not closed"):
        robot.close("gripper around peg")
    if check("the robot's gripper is closed around peg"):
        robot.pull("peg out of hole")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not closed"):
        robot.close("gripper around door handle")
    if check("the robot's gripper is closed around door handle"):
        robot.push("door closed")

# peg-unplug-sideways: push the peg out of the hole to the side
def peg_unplug_sideways(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
        robot.put("gripper