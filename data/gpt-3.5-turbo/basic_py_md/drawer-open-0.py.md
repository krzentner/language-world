```
# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")
``` 

Note that this assumes that the robot can grip the handle of the drawer and pull it open. If the drawer handle is not conducive to this motion, the code would need to be modified accordingly.