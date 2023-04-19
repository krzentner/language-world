
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is above the dial"):
        robot.turn("dial")

# valve-turn: turn the valve
# def valve_turn(robot):
    if check("the robot's gripper is not above the valve"):
        robot.put("gripper above valve")
    if check("the robot's gripper is above the valve"):
        robot.turn("valve")