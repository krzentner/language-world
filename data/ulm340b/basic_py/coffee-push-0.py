
    if check("the robot's gripper is not vertically aligned with mug and the robot's gripper is not near mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is near mug and the robot's gripper is not around mug"):
        robot.grab("mug")
    if check("the robot's gripper is near mug and the robot's gripper is not around mug"):
        robot.grab("mug")
    if check("the robot's gripper is around mug and the mug is not right of goal"):
        robot.move("mug to goal")

# coffee-pull: grab the mug and move it to the target location
def coffee_pull(robot):
    if check("the robot's gripper is not vertically aligned with mug and the robot's gripper is not near mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is near mug and the robot's gripper is not around mug"):
        robot.grab("mug")
    if check("the robot's gripper is around mug and the mug is not right of goal"):
        robot.move("mug to goal")

# coffee-button-press: push the button down from above
def coffee_button_press(robot):
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not near button"):
        robot.move("gripper to above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.put("gripper on button")
    if check("the robot's gripper is near button"):
        robot.push("down on button")

# coffee-button-side: push the button down from the side
def coffee_button_side(robot):
    if check("the robot's gripper is not horizontally aligned with button and the robot's gripper is not near button"):
        robot.move("gripper to right of button")
    if check("the robot's gripper is horizontally aligned with button and the robot's gripper is not near button"):
        robot.put("gripper on button")
    if check("the robot's gripper is near button"):
        robot.push("button left")

# scooping: grab the spoon and scoop up the powder
def scooping(robot):
    if check