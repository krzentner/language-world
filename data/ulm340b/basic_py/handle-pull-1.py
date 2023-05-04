
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above the handle"):
        robot.close("gripper around handle")
    if check("the robot's gripper is around the handle and the robot's gripper is closed"):
        robot.pull("handle up")

# handle-slide: slide the handle all the way to the right
def handle_slide(robot):
    if check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is below the handle"):
        robot.move("gripper to right of handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.slide("handle right")
    if check("the robot's gripper is in front of the handle and the handle is not right"):
        robot.push("handle right harder")

# handle-turn: turn the handle until it is fully down
def handle_turn(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above the handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is around the handle and the robot's gripper is closed"):
        robot.turn("handle counterclockwise")

# handle-turn-anticlockwise: rotate the handle in anticlockwise direction
def handle_turn_anticlockwise(robot):
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around the handle and the robot's gripper is closed"):
        robot.turn("handle counterclockwise")

# handle-turn-clockwise: rotate the handle in clockwise direction
def handle_turn_clockwise(robot):
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.put("gripper around handle")
