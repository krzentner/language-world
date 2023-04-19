# reach: reach to the target location
# def reach(robot):
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# Replace "to goal" with the specific location you want the robot to reach. Also, make sure to define the `check` function somewhere. This function should take in a string as an argument and return a boolean indicating whether or not that condition is met for the robot's gripper.