
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("door open")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# door-toggle-pull: pull the door toggle towards the robot
def door_toggle_pull(robot):
    if check("the robot's gripper is not vertically aligned with door toggle"):
        robot.put("gripper above door toggle")
    if check("the robot's gripper is vertically aligned with door toggle and the robot's gripper is not around door toggle"):
        robot.put("gripper around door toggle")
    if check("the robot's gripper is around door toggle"):
        robot.pull("door toggle towards robot")

# door-toggle-push: push the door toggle away from the robot
def door_toggle_push(robot):
    if check("the robot's gripper is not above door toggle"):
        robot.place("gripper above door toggle")
    if check("the robot's gripper is above door toggle and the robot's gripper is not near door toggle"):
        robot.move("gripper towards door toggle")
    if check("the robot's gripper is near door toggle"):
        robot.push("door toggle away")

# door-pull: pull the door open
def door_pull(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("door open")

# valve-turn: turn the valve to the desired angle
def valve_turn(robot):
