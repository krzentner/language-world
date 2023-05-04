
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle and the handle is not forward aligned with the robot's gripper"):
        robot.put("gripper around handle")
    if check("the robot's gripper is near handle and the handle is forward aligned with the robot's gripper"):
        robot.push("handle")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not forward aligned with the door handle and the robot's gripper is not behind door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is behind the door handle"):
        robot.push("door")

# door-lock: rotate the doorknob clockwise
def door_lock(robot):
    if check("the robot's gripper is not vertically aligned with the doorknob"):
        robot.place("gripper over doorknob")
    if check("the robot's gripper is vertically aligned with the doorknob and the robot's gripper is not near doorknob"):
        robot.put("gripper around doorknob")
    if check("the robot's gripper is near the doorknob"):
        robot.rotate("doorknob clockwise")

# door-unlock: rotate the doorknob counter-clockwise
def door_unlock(robot):
    if check("the robot's gripper is not vertically aligned with the doorknob"):
        robot.place("gripper over doorknob")
    if check("the robot's gripper is vertically aligned with the doorknob and the robot's gripper is not near doorknob"):
        robot.put("gripper around doorknob")
    if check("the robot's gripper is near the doorknob"):
        robot.rotate("doorknob counter-clockwise")

# handle-pull-drawer-open: grab the handle and pull the drawer open
def handle_pull_drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with the drawer handle"):
        robot.place("gripper over handle")
    if check("the robot's gripper is vertically aligned with the drawer handle and the robot's gripper is not around the drawer handle"):
        robot.grab("handle")
    if check("the robot's gripper is around the drawer