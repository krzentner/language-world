# handle-press: push down the handle
# def handle_press(robot):
def handle_press(robot):
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above the handle")
    if check("the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.drop("gripper around the handle")
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.close("gripper around the handle")
    if check("the robot's gripper is above the handle and the robot's gripper is closed"):
        robot.push("the handle down") 

# helper function to check the conditions
def check(condition):
    print("Checking if", condition)
    return True  # change to appropriate condition check code