

**If the robot's gripper is above the drawer handle**:
- the robot should `put` `the gripper around the drawer handle`
- the robot should `pull` `gripper back into drawer`

**If the robot's gripper is around the drawer handle and the robot's gripper is open**:
- the robot should `close` `gripper around drawer handle`

**If the robot's gripper is vertically aligned with drawer handle and the robot's gripper is open**:
- the robot should `put` `the gripper around the drawer handle`

**If the robot's gripper is not vertically aligned with drawer handle and the robot's gripper is closed**:
- the robot should `move` `gripper to left of drawer handle`

**If the robot's gripper is near the drawer handle and the robot's gripper is closed**:
- the robot should `push` `drawer closed`

Your code should match the code below:

```
# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is above the drawer handle"):
        robot.put("the gripper around the drawer handle")
        robot.pull("gripper back into drawer")
    if check("the robot's gripper is around the drawer handle and the robot's gripper is open"):
        robot.close("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is open"):
        robot.put("the gripper around the drawer handle")
    if check("the robot's gripper is not vertically aligned with drawer handle and the robot's gripper is closed"):
        robot.move("gripper to left of drawer handle")
    if check("the robot's gripper is near the drawer handle and the robot's gripper is closed"):
        robot.push("drawer closed")

```
'''
# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is above the drawer handle"):
        robot.put("the gripper around the drawer handle")
        robot.pull("gripper back into drawer")
    if check("the robot's gripper is around the drawer handle and the robot's gripper is open"):
        robot.close("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is open"):
        robot