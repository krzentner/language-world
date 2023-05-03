# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.put("mug above coffee machine")
    if check("the mug is above the coffee machine and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the mug is above the coffee machine and the robot's gripper is closed"):
        robot.put("mug on coffee machine")
    if check("the mug is on the coffee machine"):
        robot.slide("mug to the coffee dispenser")
    if check("the mug is below the coffee dispenser"):
        robot.put("gripper below coffee dispenser")
    if check("the mug is below the coffee dispenser and the robot's gripper is closed"):
        robot.slide("coffee into mug")
    if check("the coffee is in the mug"):
        robot.put("gripper above mug")
    if check("the mug is filled with coffee and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the mug is filled with coffee and the robot's gripper is closed"):
        robot.put("mug on coaster")