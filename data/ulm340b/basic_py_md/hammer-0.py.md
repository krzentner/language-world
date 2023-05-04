

After you submit your code, please write a comment in the forum.

```

##########################
# 4.2.2. Robot Programming (2): Hammer
#  - The robot has a single gripper that it can use to grab small objects.
#  - The following code demonstrates how the robot performs some of its tasks:
#
#```
## button-press-topdown: push the button down from above
#def button_press_topdown(robot):
#    if check("the robot's gripper is not vertically aligned with button"):
#        robot.put("gripper above button")
#    if check("the robot's gripper is vertically aligned with button"):
#        robot.push("down on button")
#
## door-open: pull the door open
#def door_open(robot):
#    if check("the robot's gripper is not almost vertically aligned with door handle"):
#        robot.put("gripper above door handle")
#    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
#        robot.put("gripper around door handle")
#    if check("the robot's gripper is vertically aligned with the door handle"):
#        robot.pull("door open")
#
## reach: reach to the target location
#def reach(robot):
#    if check("the robot's gripper is not near reach target"):
#        robot.reach("to goal")
#
## drawer-close: push the drawer close
#def drawer_close(robot):
#    if check("the robot's gripper is not near the drawer handle"):
#        robot.grab("drawer handle")
#    if check("the robot's gripper is forward aligned with drawer handle"):
#        robot.push("drawer closed")
#
## drawer-open: pull the drawer open
#def drawer_open(robot):
#    if check("the robot's gripper is not vertically aligned with drawer handle"):
#        robot.put("gripper above drawer handle")
#    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
#        robot.put("gripper around drawer handle")
#    if check("the robot's gripper is around drawer handle"):
#        robot.pull("away from drawer")
#
## peg-insert-side: grab the peg and insert it into the hole