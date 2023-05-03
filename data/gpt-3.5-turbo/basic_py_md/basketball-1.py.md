# basketball: put the ball into the hoop
def basketball(robot):
    if check("the ball is not in the robot's gripper"):
        robot.grab("the ball")
    if check("the robot's gripper is not near the hoop"):
        robot.reach("the hoop")
    if check("the robot's gripper is near the hoop"):
        robot.put("the ball into the hoop")
        
Note: The `check` function is not defined in the given code, so I assumed that it is a helper function that checks a certain condition and returns True or False. The `robot` object is also assumed to have the necessary methods (`grab`, `reach`, `put`) to perform the task.