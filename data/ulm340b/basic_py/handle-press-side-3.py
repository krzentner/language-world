
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is forward aligned with handle"):
        robot.push("down on handle")


# handle-press-topdown: push the handle down from above
def handle_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not near handle"):
        robot.move("gripper to handle")
    if check("the robot's gripper is near handle"):
        robot.push("down on handle")

# reach-pick-place: reach to the puck, pick it up, and place it at the target
def reach_pick_place(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above the puck"):
        robot.place("gripper around puck")
    if check("the robot's gripper is below the puck"):
        robot.place("puck at target")

# button-press-side: push the button down from the side
def button_press_side(robot):
    if check("the robot's gripper is not almost vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move("gripper to button")
    if check("the robot's gripper is almost horizontally aligned with the button"):
        robot.push("down on button")

# dial-turn-clockwise: turn the dial clockwise
def dial_turn_clockwise(robot):
    if check("the robot's gripper is not forward aligned with dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is horizontally aligned with dial"):
        robot.grab("dial")
    if check("the robot's gripper is forward aligned with dial"):
        robot.turn("dial clockwise")

# dial-turn-counterclockwise: turn the dial counter clockwise
def dial_turn_counterclockwise(robot):
    if check("the robot's gripper is not forward aligned with dial"):
