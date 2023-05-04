

The `coffee-button` function should use one or more of the following `check` conditions:

`robot's gripper is not above the coffee machine button`

`robot's gripper is above coffee machine button and robot's gripper is not closed`

`robot's gripper is above coffee machine button and robot's gripper is closed`

Use the robot action `press(object)` to push the button.

---
# 3)

Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# window-close: slide the window closed to the right
def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
       