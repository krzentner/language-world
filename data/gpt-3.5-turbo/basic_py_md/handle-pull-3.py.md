```
# handle-pull: pull up the handle
def handle_pull(robot):
    if check("the robot's gripper is not near handle"):
        robot.move("gripper to handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")
``` 

This code checks if the robot's gripper is near the handle. If it is not near, it will move the gripper to the handle. Then it checks if the gripper is vertically aligned with the handle and if the gripper is open. If both are true, the gripper will close around the handle. Finally, if the gripper is around the handle, it will pull up the handle.