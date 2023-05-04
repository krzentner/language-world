
    if check("the robot's gripper is not vertically aligned with wrench and the robot's gripper is above wrench"):
        robot.place("gripper above wrench")
    if check("the robot's gripper is above wrench and the robot's gripper is not around wrench"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is around wrench"):
        robot.pull("gripper up")

# pick-place-into-object: pick up the puck and place it on the blue cube
def pick_place_into_object(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck above blue cube")
    if check("the robot's gripper is not above the blue cube and the robot's gripper is below blue cube"):
        robot.put("gripper above blue cube")
    if check("the robot's gripper is above blue cube"):
        robot.drop("puck onto blue cube")

# pick-place-into-object2: pick up the puck and place it inside the blue cube
def pick_place_into_object2(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck above blue cube")
    if check("the robot's gripper is not vertically aligned with blue cube"):
        robot.move("gripper to be vertically aligned with blue cube")
    if check("the robot's gripper is vertically aligned with blue cube"):
        robot.put("puck in blue cube")

# pick-place-into-object3: pick up the puck and place it on top of the blue cube
def pick_place_into_object3(robot):
    if check("the robot's gripper is not above the puck