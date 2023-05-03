# door-open: pull the door open
# def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not mostly vertically aligned with door handle"):
        robot.put("gripper above door handle")
   
    # As long as the gripper is almost lined up, closing it should line it up all the way.
    if check("the robot's gripper is mostly vertically aligned with door handle and the robot's gripper is open"):
        robot.drop("gripper around door handle")
    
    # As long as the gripper is still mostly around the door handle, it's being opened, so keep pulling.
    if check("the robot's gripper is mostly around door handle"):
        robot.pull("door open")