```
# door-open: pull the door open
# def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still vertically aligned with the door handle,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")
``` 

This program will first check if the gripper is above the door handle, if not it will move the gripper above the handle. Next, it will check if the gripper is almost vertically aligned with the handle, and if it is, it will drop the gripper around the handle. Finally, it will check if the gripper is vertically aligned with the handle, and if it is, it will pull the door open.