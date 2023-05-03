

# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is around mug and the robot's gripper is closed"):
        robot.move("mug to goal")