
Here is the program for the door-open task:

# door-open: pull the door open 
def door_open(robot): 
    if check("the robot's gripper is not almost vertically aligned with door handle"): 
        robot.put("gripper above door handle") 
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"): 
        robot.put("gripper around door handle") 
    if check("the robot's gripper is vertically aligned with the door handle"): 
        robot.pull("door open")