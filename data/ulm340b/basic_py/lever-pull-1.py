
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever"):
        robot.grab("lever")
    if check("the robot's gripper is around lever and the lever is not vertical"):
        robot.rotate("lever up")

# valve-open: turn the valve to the left
def valve_open(robot):
    if check("the robot's gripper is not vertically aligned with the valve"):
        robot.put("gripper above valve")
    if check("the robot's gripper is not near valve"):
        robot.move("gripper into valve")
    if check("the robot's gripper is near valve"):
        robot.rotate("valve left")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")

# peg-unstack: pick up the top peg
def peg_unstack(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not near peg"):
        robot.place("gripper on top of peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is forward aligned with peg"):
        robot.lift("peg off table")

# valve-close: turn the valve to the right
def valve_close(robot):
    if check("the robot's gripper is not vertically aligned with valve"):
        robot.put("gripper above valve")
    if check("the robot's gripper is not near valve"):
        robot.move("gripper into valve")
    if check("the robot's gripper is near valve"):
        robot