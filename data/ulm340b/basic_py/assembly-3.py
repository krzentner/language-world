
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("the gripper above the wrench")
    if check("the robot's gripper is vertically aligned with wrench"):
        robot.put("gripper around wrench")
    if check("the robot's gripper is around wrench"):
        robot.put("wrench around peg")

# switch-on: push the switch up
def switch_on(robot):
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch"):
        robot.slide("switch upwards")

# button-press-side: push the button in sideways
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button in")



# push: slide the puck to the target location
def task_push(robot):
    if check("the robot's gripper is not above puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.slide("the puck to the goal")

# button-press-topdown: push the button down from above
def task_button_press_topdown(robot):
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    if check("the robot's gripper is not vertically aligned with button"):
        robot.push("down on button")

# reach: reach to the target location
def task_reach(robot):
    if check("the robot's gripper is not above reach target"):
        robot.put("gripper above reach target")
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# door-open: pull the door open
def task_door_open(robot):
    if check("the robot's gripper is not above door handle"):
        robot.put("gripper