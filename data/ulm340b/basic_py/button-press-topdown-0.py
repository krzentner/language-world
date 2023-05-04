
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is above the button and the robot's gripper is not vertically aligned with the button"):
        robot.move("gripper to align with button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.push("gripper onto button")
    if check("the robot's gripper is above the button and the robot's gripper is vertically aligned with the button"):
        robot.push("the button down")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move("gripper to align with door handle")
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.push("door closed")

# peg-insert-side-experiment-v1: grab the peg and insert it into the hole from the side
def peg_insert_side_experiment_v1(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# peg-unstack: unstack the peg
def peg_unstack(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to