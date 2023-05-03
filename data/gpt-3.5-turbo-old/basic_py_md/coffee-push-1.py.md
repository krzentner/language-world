# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    if check("the robot's gripper is not above the coffee mug"):
        robot.place("gripper above coffee mug")
    if check("the robot's gripper is not around coffee mug and the robot's gripper is open"):
        robot.drop("gripper around coffee mug")
    if check("the robot's gripper is near coffee mug and the robot's gripper is open"):
        robot.close("gripper around coffee mug")
    if check("the robot's gripper is above coffee mug and the robot's gripper is closed"):
        robot.move("the coffee mug to the target location")