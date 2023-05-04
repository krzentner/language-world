
    if check("the robot's gripper is not above peg"):
        robot.move("gripper above peg")
    if check("the robot's gripper is above peg and the robot's gripper is open"):
        robot.place("gripper around peg")
    if check("the robot's gripper is around peg and the peg is above the robot's gripper"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.grab("the peg")
    if check("the robot's gripper is in front of hole and the robot's gripper is closed"):
        robot.insert("peg into hole")

# knob-turn-left: grab the handle and rotate it left
def knob_turn_left(robot):
    if check("the robot's gripper is not above the knob handle"):
        robot.move("gripper above handle")
    if check("the robot's gripper is above the knob handle and the robot's gripper is open"):
        robot.place("gripper around knob handle")
    if check("the robot's gripper is around the knob handle and the knob handle is above the robot's gripper"):
        robot.close("gripper around knob handle")
    if check("the robot's gripper is around the knob handle"):
        robot.turn("left")

# knob-turn-right: grab the handle and rotate it right
def knob_turn_right(robot):
    if check("the robot's gripper is not above the knob handle"):
        robot.move("gripper above handle")
    if check("the robot's gripper is above the knob handle and the robot's gripper is open"):
        robot.place("gripper around knob handle")
    if check("the robot's gripper is around the knob handle and the knob handle is above the robot's gripper"):
        robot.close("gripper around knob handle")
    if check("the robot's gripper is around the knob handle"):
        robot.turn("right")

# pick-place-wall: pick up the puck and place it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above