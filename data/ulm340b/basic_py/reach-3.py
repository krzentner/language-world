
    if check("the robot's gripper is not above target"):
        robot.put("gripper above target")

# release: drop the object
def release(robot):
    if check("the robot's gripper is not open and the robot's gripper is holding the object"):
        robot.release("object")

# retract: move gripper back
def retract(robot):
    if check("the robot's gripper is not retracted"):
        robot.retract("gripper")

# slide: push puck around horizontally
def slide(robot):
    if check("the robot's gripper is not forward aligned with the puck"):
        robot.align("gripper to puck")
    if check("the robot's gripper is forward aligned with puck and the robot's gripper is not near puck"):
        robot.move("gripper into puck")
    if check("the robot's gripper is near the puck and the puck is right of the robot's gripper"):
        robot.push("puck right")
    if check("the robot's gripper is near the puck and the puck is in front of the robot's gripper"):
        robot.push("puck right harder")

# torque-peg-side: grab the peg and push it down into the hole from the side
def torque_peg_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.torque("peg into hole")

# unplug-side: grab the plug and pull it out of the socket from the side
def unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the plug and the robot's gripper is above the plug"):
        robot.move("gripper to left of plug")
    if check("the robot's gripper is vertically aligned with the plug and the plug is not left of the robot's gripper and the plug is not forward aligned with the robot's gripper"):
        robot.grab("plug")
