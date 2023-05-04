
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.push("door closed")

# turn-lever-down: pull the lever to the down position
def turn_lever_down(robot):
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever"):
        robot.grab("lever")
    if check("the robot's gripper is around lever"):
        robot.rotate("lever down")

# turn-switch-left: turn the switch to the left position
def turn_switch_left(robot):
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch"):
        robot.grab("switch")
    if check("the robot's gripper is around switch"):
        robot.rotate("switch left")

# rotate-tray: rotate the tray counterclockwise to the end
def rotate_tray(robot):
    if check("the robot's gripper is not vertically aligned with tray"):
        robot.put("gripper above tray")
    if check("the robot's gripper is vertically aligned with tray"):
        robot.grab("tray")
    if check("the robot's gripper is around tray"):
        robot.rotate("tray counterclockwise")

# drawer-insert-side: grab the drawer and insert it into the cabinet from the side
def drawer_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with drawer"):
        robot.put("gripper above drawer")
    if check("the robot's gripper is vertically aligned with drawer and the robot's gripper is not forward aligned with drawer"):
        robot.grab("drawer")
    if check("the robot's gripper is forward aligned with drawer and the drawer is not horizontally aligned with cabinet"):
        robot.align("drawer to cabinet")
    if check("the drawer is horizontally aligned with cabinet