# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not above the mug"):
        robot.place("gripper above the mug")
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around the mug")
    if check("the robot's gripper is near the mug and the robot's gripper is open"):
        robot.close("gripper around the mug")
    if check("the robot's gripper is above the mug and the mug is not on the goal"):
        robot.lift("the mug")
        robot.move("the mug to the goal")
    if check("the mug is on the goal"):
        robot.put("the mug on the goal")