

# 1. Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.
# 2. Here's some code that demonstrates how the robot can do a variety of tasks:
# 3.```
# 4.# reach: reach to the target location
# 5.def reach(robot):
# 6.    if check("the robot's gripper is not near reach target"):
# 7.        robot.reach("to goal")
# 8.
# 9.# door-open: pull the door open
# 10.def door_open(robot):
# 11.    if check("the robot's gripper is not almost vertically aligned with door handle"):
# 12.        robot.put("gripper above door handle")
# 13.    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
# 14.        robot.put("gripper around door handle")
# 15.    if check("the robot's gripper is vertically aligned with the door handle"):
# 16.        robot.pull("door open")
# 17.
# 18.# drawer-close: push the drawer close
# 19.def drawer_close(robot):
# 20.    if check("the robot's gripper is not near the drawer handle"):
# 21.        robot.grab("drawer handle")
# 22.    if check("the robot's gripper is forward aligned with drawer handle"):
# 23.        robot.push("drawer closed")
# 24.
# 25.# push: slide the puck to the target location
# 26.def push(robot):
# 27.    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
# 28.        robot.put("the gripper above the puck")
# 29.    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
# 30.        robot.push("the gripper into the puck")
# 31.    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
# 32.        robot.slide("