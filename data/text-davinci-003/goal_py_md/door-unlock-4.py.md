

Steps:
 1. Put gripper on top of door handle  
 2. Grip the door handle with gripper
 3. Turn the gripper clockwise to unlock the door

```
# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper on top of door handle
    #  2. Grip the door handle with gripper
    #  3. Turn the gripper clockwise to unlock the door
   
    # First, put the gripper above the door handle 
    if check("the robot's gripper is not above the door handle"):
        robot.move_gripper("above the door handle", close_gripper=True)
    # Next, turn the gripper clockwise to grip the handle
    if check("the robot's gripper is not in front of the door handle"): 
        robot.move_gripper("in front of the door handle")
    # Finally, rotate the gripper clockwise to unlock the door
    if check("the robot's gripper is in front of the door handle"):
        robot.rotate_gripper("clockwise")