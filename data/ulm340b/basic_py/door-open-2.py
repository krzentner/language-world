
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# turn-switch-on: move the switch from the off position to the on position
def turn_switch_on(robot):
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch and the robot's gripper is not left of switch"):
        robot.move("gripper to left of switch")
    if check("the robot's gripper is left of switch"):
        robot.toggle("switch on")

# turn-switch-off: move the switch from the on position to the off position
def turn_switch_off(robot):
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch and the robot's gripper is not left of switch"):
        robot.move("gripper to left of switch")
    if check("the robot's gripper is left of switch"):
        robot.toggle("switch off")

# pick-heat: pick up the pot and place it on the target location
def pick_heat(robot):
    if check("the robot's gripper is not above the pot handle"):
        robot.place("gripper above pot handle")
    if check("the robot's gripper is above the pot handle and the robot's gripper is not around the pot handle"):
        robot.drop("gripper around pot handle")
    if check("the robot's gripper is around the pot handle"):
        robot.pick("up the pot")
    if check("the robot