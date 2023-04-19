# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.move("gripper to the target location")
        robot.grab("target")
        robot.lift("target")
        robot.move("target to goal")
        robot.release("target at goal")