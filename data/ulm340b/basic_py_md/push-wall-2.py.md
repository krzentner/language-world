

Then fill in some code to accomplish the `push-wall` task.
For the final line, please write `return()`.
If this is your first time with this task, please just ask me for a hint.
Thanks!
"""

def push_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck"):
        robot.grab("puck")
    if check("the robot's gripper is above puck and the puck is not above the wall"):
        robot.move("puck above wall")
    if check("the puck is above the wall"):
        robot.drop("puck above wall")
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    if check("the robot's gripper is above the wall"):
        robot.move("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is not near puck"):
        robot.push("gripper into puck")
    if check("the robot's gripper is near puck and the puck is below the robot's gripper"):
        robot.slide("puck to goal")
    if check("the puck is at the goal"):
        return()

"""
# Example 3
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")

# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned