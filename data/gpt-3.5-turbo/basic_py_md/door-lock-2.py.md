# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not near the dial"):
        robot.put("gripper near the dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not around the dial"):
        robot.grab("the dial")
    if check("the robot's gripper is around the dial and the dial is not aligned with the lock"):
        robot.align("dial to lock")
    if check("the dial is aligned with the lock"):
        robot.turn("the dial to lock it") 

Note: `check()` is a function that checks if a condition is true and executes the appropriate action. This function is not provided in the given code.