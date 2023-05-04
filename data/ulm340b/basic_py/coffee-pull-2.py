
    if check("the robot's gripper is not above the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is not closed around the mug and the robot's gripper is above the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is closed around the mug and the robot's gripper is forward aligned with the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is above the mug"):
        robot.place("the mug at the goal")

# coffee-push: grab the mug and push it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not above the mug and the robot's gripper is not near the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is not closed around the mug and the robot's gripper is above the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is closed around the mug and the robot's gripper is forward aligned with the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is above the mug"):
        robot.place("the mug at the goal")

# coffee-open: hold the mug and twist it open
def coffee_open(robot):
    if check("the robot's gripper is not near the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is not closed around the mug and the robot's gripper is forward aligned with the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is closed around the mug and the robot's gripper is above the mug"):
        robot.twist("the mug open")

# coffee-close: hold the mug and twist it closed
def coffee_close(robot):
    if check("the robot's gripper is not near the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is not closed around the mug and the robot's gripper is forward aligned with the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is closed around the mug and the robot's gripper is above the mug"):
        robot.twist("the mug closed")

# door-lock: