

You can use the command `robot.place("gripper near plate")` to move the gripper near the plate,
and `robot.push("gripper into plate")` to push the plate into the target position.
The `robot.slide("plate to goal")` should be used to finish the task.
"""

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not below plate"):
        robot.place("gripper near plate")
    if check("the robot's gripper is below plate and the robot's gripper is open"):
        robot.place("gripper around plate")
    if check("the robot's gripper is below plate"):
        robot.push("gripper into plate")
    if check("plate is left of goal"):
        robot.slide("plate to goal")

"""
## Example 2:

Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if