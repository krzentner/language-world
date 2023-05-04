
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button")

# pick: pick up the puck
def pick(robot):
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.close("gripper around puck")

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place_with_camera(robot):
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# slider-button: push the button on the slider
def slider_button(robot):
    if check("the robot's gripper is not above slider"):
        robot.put("gripper above slider")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is above slider"):
        robot.press("button")

# pick-place-wall: pick up the puck and hold it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# coffee-button-side: push the button on the coffee machine from the side
def coffee_button_side(robot):
    if check("the robot's gripper is below button"):
        robot.put("gripper to side of button")
    if check("the robot's gripper is to the side of button"):
        robot.press