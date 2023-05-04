
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above the puck and the puck is below the robot's gripper"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# push-back: push the box to the target location
def push_back(robot):
    if check("the robot's gripper is not above the box and the robot's gripper is not vertically aligned with the box"):
        robot.put("gripper above box")
    if check("the robot's gripper is vertically aligned with the box and the robot's gripper is not near box"):
        robot.push("gripper into box")
    if check("the robot's gripper is near the box and the box is below the robot's gripper"):
        robot.slide("box to goal")

# pick-place-back: pick up the box and hold it at the target location
def pick_place_back(robot):
    if check("the robot's gripper is not above the box"):
        robot.place("gripper above box")
    if check("the robot's gripper is not around box and the robot's gripper is open"):
        robot.drop("gripper around box")
    if check("the robot's gripper is near box and the robot's gripper is open"):
        robot.close("gripper around box")
    if check("the robot's gripper is above box and the robot's gripper is closed"):
        robot.place("box at goal")

# pick-place-bin: pick up the object and hold it at the target location inside the basket
def pick_place_bin(robot):
    if check("the robot's gripper is not above the object"):
        robot.place("gripper above object")
    if check("the robot's gripper is not around object and the robot's gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is near object and the robot's gripper is