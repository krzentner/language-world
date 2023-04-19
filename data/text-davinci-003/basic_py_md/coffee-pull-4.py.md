

Solution: 

# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above the mug")
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.grab("gripper around mug")
    if check("the robot's gripper is around mug and the robot's gripper is close"):
        robot.pull("the mug to the goal")