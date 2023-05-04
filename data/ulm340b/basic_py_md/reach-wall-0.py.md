

You should also call `robot.open_grip()` at the beginning of the function.
"""

# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    robot.open_grip()
    if check("the robot's gripper is not near the reach target"):
        robot.reach("over wall")
    if check("the robot's gripper is on the short wall"):
        robot.move("to wall")
    if check("the robot's gripper is near the wall"):
        robot.over_wall("to goal")

##########################################################################################
print()
print("===")
print("Level 2")
print()

print("Hello. Today I would like you to help me control a robot. The robot has two grippers that it can use to grab small objects.")

print()
print("Here's some code that demonstrates how the robot can do a variety of tasks:")
print()

print("""# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not near drawer handle"):
        robot.move("gripper to left of drawer handle")
    if check("the robot's gripper is near drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")

# window-open: slide the window open to the left
def window_open(robot):
    if check("the robot's gripper is not near window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near window handle"):
        robot.grab("window handle")
    if check("the robot's gripper is forward aligned with window handle"):
        robot.slide("window left")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not near door handle"):
        robot.move("gripper to left of door handle")
    if check("the robot's gripper is near door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.pull("door open")

# window-close: slide the window closed to the right
def window_close(robot):
