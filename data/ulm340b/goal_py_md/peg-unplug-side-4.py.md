

If you get stuck, you can ask for hints.

"""


# peg-unplug-side: grab the peg and pull the it out from the side
def peg_unplug_side(robot):
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # If the robot's gripper is vertically aligned with the peg, grip it.
    if check("the peg is vertically aligned with the robot's gripper"):
        robot.move_gripper("above the peg", close_gripper=True)
    # If the robot's gripper is above the peg, start pulling the peg out from
    # the hole.
    if check("peg is above the robot's gripper"):
        robot.move_gripper("above the peg", close_gripper=True)

# These functions are here so that we can test the functions one at a time
def drawer_close(robot):
    print("The task 'drawer-close' is not yet implemented.")
    robot.task_done()

def button_press_topdown(robot):
    print("The task 'button-press-topdown' is not yet implemented.")
    robot.task_done()

def drawer_open(robot):
    print("The task 'drawer-open' is not yet implemented.")
    robot.task_done()

def door_open(robot):
    print("The task 'door-open' is not yet implemented.")
    robot.task_done()

def reach(robot):
    print("The task 'reach' is not yet implemented.")
    robot.task_done()

def window_open(robot):
    print("The task 'window-open' is not yet implemented.")
    robot.task_done()

def window_close(robot):
    print("The task 'window-close' is not yet implemented.")
    robot.task_done()

def push(robot):
    print("The task 'push' is not yet implemented.")
    robot.task_done()

def pick_place(robot):
    print("The task 'pick-place' is not yet implemented.")
    robot.task_done()

def peg_insert_side(robot):