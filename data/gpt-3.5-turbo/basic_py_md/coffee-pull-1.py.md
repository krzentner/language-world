# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    if check("the robot's gripper is not above the mug"):
        robot.place("gripper above mug")
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        if check("the mug's handle is facing towards the target location"):
            robot.pull("mug to goal")
        else:
            robot.rotate("mug until handle is towards goal")
            robot.pull("mug to goal")