
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is not around the wrench"):
        robot.put("gripper around wrench")
    if check("the robot's gripper is around the wrench and the robot's gripper is open"):
        robot.close("gripper around wrench")
    if check("the robot's gripper is closed around the wrench"):
        robot.pull("wrench off peg")

# button-press-side: push the button in from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not around button"):
        robot.put("gripper around button")
    if check("the robot's gripper is around button"):
        robot.push("in button")

# button-press-topdown-side: push the button down from above
def button_press_topdown_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not forward aligned with button"):
        robot.align("gripper to button")
    if check("the robot's gripper is forward aligned with button and the robot's gripper is not around button"):
        robot.put("gripper around button")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("in button")


# TASK DEFINITIONS: tasks that need to be done
def execute_task(task, robot):
    if task == "reach":
        reach(robot)
    elif task == "push":
        push(robot)
    elif task == "button_press_topdown":
        button_press_topdown(robot)
    elif task == "drawer_close":
        drawer_close(robot)
    elif task == "pick_place":
        pick_place(robot)
    elif task == "window_open":
        window_open(robot)
    elif task == "door_open":
        door_open(robot)
    elif task == "drawer_open":
       