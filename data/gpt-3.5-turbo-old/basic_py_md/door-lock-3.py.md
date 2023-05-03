# door-lock: turn the dial on the door
# def door_lock(robot):
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to the right of the dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above the dial")
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.grab("the dial")
        robot.rotate("the dial right by 3 full turns") #assuming three turns will lock it
