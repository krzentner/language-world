
    if check("the robot's gripper is not vertically aligned with block and the robot's gripper is not near block"):
        robot.place("gripper above block")
    if check("the robot's gripper is above block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is around block and the robot's gripper is closed"):
        robot.place("block at goal")

# drawer-close: push the drawer closed
def drawer_close(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not near drawer handle"):
        robot.push("gripper into drawer handle")
    if check("the robot's gripper is near drawer handle and the robot's gripper is not around drawer handle"):
        robot.close("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("drawer closed")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not near door handle"):
        robot.push("gripper into door handle")
    if check("the robot's gripper is near door handle and the robot's gripper is not around door handle"):
        robot.close("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("door open")

# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not near drawer handle"):
        robot.push("gripper into drawer handle")
    if check("the robot's gripper is near drawer handle and the robot's gripper is not around drawer handle"):
        robot.close("gripper around drawer handle")
  