
    if check("the robot's gripper is not near the button"):
        robot.reach("towards button")
    if check("the robot's gripper is near the button"):
        robot.push("button into wall")

# button-press-side: push the button from the front
def button_press_side(robot):
    if check("the robot's gripper is not near the button and the robot's gripper is not near the button"):
        robot.reach("towards button")
    if check("the robot's gripper is near the button"):
        robot.push("button sideways")

# button-press-top: push the button from the front
def button_press_top(robot):
    if check("the robot's gripper is not near the button and the robot's gripper is not near the button"):
        robot.reach("towards button")
    if check("the robot's gripper is near the button"):
        robot.push("button sideways")

# hook-hang: pick up the hook and hang it to the target
def hook_hang(robot):
    if check("the robot's gripper is not above hook"):
        robot.move("gripper above hook")
    if check("the robot's gripper is above hook"):
        robot.place("gripper around hook")
    if check("the robot's gripper is around hook"):
        robot.grab("hook")
    if check("the robot's gripper is around hook and the robot's gripper is forward aligned with hook"):
        robot.hang("hook to target")

# hang-clean: pick up the hanger and hang it to the target
def hang_clean(robot):
    if check("the robot's gripper is not above hanger"):
        robot.put("gripper above hanger")
    if check("the robot's gripper is above hanger"):
        robot.place("gripper around hanger")
    if check("the robot's gripper is around hanger"):
        robot.grab("hanger")
    if check("the robot's gripper is around hanger and the robot's gripper is vertically aligned with hanger"):
        robot.hang("hanger to target")

# drawer-pull-out: pull the drawer open
def drawer_pull_out(robot):
    if check("the robot's gripper is not vertically aligned with the drawer handle"):
        robot.put