
    if check("the robot's gripper is not above handle"):
        robot.move("gripper above handle")
    if check("the robot's gripper is above handle"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")

# handle-press: push down the handle
def handle_press(robot):
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.push("handle down")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not above the door handle and the robot's gripper is not below the door handle"):
        robot.move("gripper near door handle")
    if check("the robot's gripper is below the door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is below the door handle"):
        robot.push("door closed")

# valve-turn: rotate the valve
def valve_turn(robot):
    if check("the robot's gripper is not vertically aligned with valve handle"):
        robot.put("gripper above valve handle")
    if check("the robot's gripper is above valve handle and the robot's gripper is open"):
        robot.put("gripper around valve handle")
    if check("the robot's gripper is vertically aligned with valve handle and the robot's gripper is around valve handle"):
        robot.turn("valve clockwise")

# pick-place-wall: pick up the block and place it next to the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not above block"):
        robot.put("gripper above block")
    if check("the robot's gripper is above block"):
        robot.drop("gripper around block")
    if check("the robot's gripper is around block"):
        robot.close("gripper around block")
    if check("the robot's gripper is around block and the robot's gripper is closed"):
