
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is left of the button"):
        robot.push("gripper into button")
    if check("the robot's gripper is forward aligned with the button"):
        robot.press("button down")

# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not forward aligned with the button"):
        robot.push("gripper into button")
    if check("the robot's gripper is forward aligned with the button"):
        robot.press("button down")

# peg-unstack-side: grab the peg at the middle and place the peg at the goal location
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("the robot's gripper is near peg"):
        robot.grab("peg")
    if check("peg is forward aligned with the robot's gripper and peg is not placed at goal"):
        robot.place("peg at goal")

# pick-place-wall: pick the puck up and hold it at the target location, behind a wall that is in the way
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("