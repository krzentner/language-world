
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is not forward aligned with button"):
        robot.push("the button forward")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("the button down")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near door handle"):
        robot.push("door closed")

# peg-unstack-side: lift the top two pegs from the stack from the side
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with the top peg"):
        robot.put("the gripper above the top peg")
    if check("the top peg is not left of the robot's gripper and the top peg is not forward aligned with the robot's gripper"):
        robot.grab("the top peg")
    if check("the robot's gripper is forward aligned with the top peg and the top peg is not vertically aligned with the bottom peg"):
        robot.lift("the top peg above the bottom peg")

# peg-remove-side: pull the peg from the hole from the side
def peg_remove_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg and the robot's gripper is not near the peg"):
        robot.grab("the peg")
    if check("the robot's gripper is near the peg and the robot's gripper is not around peg"):
        robot.pull("peg out of hole")

# valve-open: turn the valve open
def valve_open(robot):
    if check("the robot's gripper is not near valve"):
        robot.put("gripper around valve")
    if check("the robot's gripper is near valve"):
        robot.twist("valve open")

# valve-close: turn the valve closed
def valve_close(robot):
    if check("the robot's gripper is not near valve"):
        robot.put("gripper around valve")
    if check("the robot's gripper is near valve"):
        robot.twist("valve closed")

