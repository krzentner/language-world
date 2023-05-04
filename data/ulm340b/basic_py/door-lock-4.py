
    if check("the robot's gripper is not near the door dial"):
        robot.put("gripper above door dial")
    if check("the robot's gripper is vertically aligned with the door dial"):
        robot.twist("door dial clockwise")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door"):
        robot.put("gripper near door")
    if check("the robot's gripper is in front of the door and the robot's gripper is open"):
        robot.close("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is open"):
        robot.push("door closed")

# peg-unplug-side: grab the peg and remove it from the hole
def peg_unplug_side(robot):
    if check("the robot's gripper is not near the peg"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with the hole"):
        robot.align("peg with hole")
    if check("the peg is horizontally aligned with the hole"):
        robot.pull("peg out of hole")
    if check("the peg is near the robot's gripper and the peg is not above the robot's gripper"):
        robot.pull("peg above gripper")
    if check("the peg is above the robot's gripper"):
        robot.release("peg")

# pick: pick up the puck
def pick(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the puck is below the robot's gripper"):
        robot.grab("puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck and puck is near robot's gripper"):
        robot.grab("puck")
    if check("the robot's gripper is above puck and the puck is near the robot's gripper"):
        robot.pick("up puck")

#