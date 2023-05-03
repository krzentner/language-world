# Approach 1: Incremental dial turning
# def dial_turn(robot, direction):
#     if check("the robot's gripper is not aligned with the dial"):
#         robot.align("gripper to dial")
#     if direction == "clockwise":
#         robot.turn("dial clockwise")
#     elif direction == "counterclockwise":
#         robot.turn("dial counterclockwise")
#     elif direction == "random":
#         robot.turn("dial either way")

# Approach 2: Specify number of turns
def dial_turn(robot, turns):
    if check("the robot's gripper is not aligned with the dial"):
        robot.align("gripper to dial")
    if turns > 0:
        robot.turn("dial clockwise")
        dial_turn(robot, turns-1)
    elif turns < 0:
        robot.turn("dial counterclockwise")
        dial_turn(robot, turns+1)