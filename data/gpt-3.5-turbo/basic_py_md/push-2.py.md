# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not near the puck and the robot's gripper is open"):
        robot.move("gripper to the left of the puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around the puck")
    if check("the robot's gripper is around the puck and it is not vertically aligned with the target location"):
        robot.align("puck to the target")
    if check("the puck is vertically aligned with the target location"):
        robot.slide("puck to the goal")
    if check("the puck has reached the target location"):
        robot.open("gripper")