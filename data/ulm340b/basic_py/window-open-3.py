
    if check("the robot's gripper is left of the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is right of the window handle"):
        robot.push("window left")


# Tasks
def task_0(robot):
    robot.say_task("Task 0")
    [pick_place(robot), reach(robot), pick_place(robot), reach(robot)]

def task_1(robot):
    robot.say_task("Task 1")
    [pick_place(robot), button_press_topdown(robot), pick_place(robot), reach(robot)]

def task_2(robot):
    robot.say_task("Task 2")
    [pick_place(robot), button_press_topdown(robot), pick_place(robot), reach(robot), window_close(robot), window_open(robot)]

def task_3(robot):
    robot.say_task("Task 3")
    [pick_place(robot), button_press_topdown(robot), pick_place(robot), reach(robot), window_close(robot), window_open(robot), drawer_close(robot), drawer_open(robot), window_close(robot), window_open(robot), door_open(robot), reach(robot)]

def task_4(robot):
    robot.say_task("Task 4")
    [pick_place(robot), button_press_topdown(robot), pick_place(robot), reach(robot), window_close(robot), window_open(robot), door_open(robot), reach(robot)]

def task_5(robot):
    robot.say_task("Task 5")
    [pick_place(robot), reach(robot), peg_insert_side(robot), pick_place(robot), reach(robot), door_open(robot)]

def task_6(robot):
    robot.say_task("Task 6")
    [pick_place(robot), reach(robot), peg_insert_side(robot), pick_place(robot), reach(robot), drawer_close(robot)]

def task_7(robot):
    robot.say_task("Task 7")
    [pick_place(robot), window_close(robot), window_open(robot), drawer_close(robot)]

def task_8(robot):
    robot.say_task("Task 8")
    [pick_place(