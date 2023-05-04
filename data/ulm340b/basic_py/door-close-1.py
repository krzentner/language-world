
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near door handle and the robot's gripper is open"):
        robot.close("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")

# drawer-insert: slide the drawer closed to the target location
def drawer_insert(robot):
    if check("the robot's gripper is not vertically aligned with the drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with the drawer handle and the robot's gripper is not near drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is near drawer handle and the robot's gripper is open"):
        robot.close("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("drawer closed")

# window-close: slide the window closed to the target location
def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# window-open: slide the window open to the target location
def window_open(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# peg-unstack-topdown: pick up the top peg
def peg_