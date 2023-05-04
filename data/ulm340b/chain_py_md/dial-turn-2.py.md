

Then write code under that line to get the robot to turn the dial to be flat with the surface.
*/

# dial-turn: turn the dial
def dial_turn(robot):

    # Steps:
    #  1. Put gripper around the dial
    #  2. Rotate the dial clockwise
    #  3. Rotate the dial counterclockwise
    #  4. Rotate the dial clockwise
    if check("the robot's gripper is not around the dial"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial and the dial is not in the final position"):
        robot.turn("dial clockwise")
    if check("the robot's gripper is around the dial and the dial is not in the final position"):
        robot.turn("dial counterclockwise")
    if check("the robot's gripper is around the dial and the dial is not in the final position"):
        robot.turn("dial clockwise")

# Rotate the dial clockwise
def turn(obj):
    # First we move the dial to the goal
    if check("the robot's gripper is around " + str(obj) + " and " + str(obj) + " is not in the final position"):
        move(obj + " to goal")

# Rotate the dial counterclockwise
def turn(obj):
    # First we move the dial to the goal
    if check("the robot's gripper is around " + str(obj) + " and " + str(obj) + " is not in the final position"):
        move(obj + " to goal")


# put gripper above the peg
def put(obj):
    if check("the robot's gripper is not vertically aligned with " + str(obj) + " and the robot's gripper is not near " + str(obj)):
        move(obj + " to goal")

# put gripper above the button
def put(obj):
    if check("the robot's gripper is not vertically aligned with " + str(obj) + " and the robot's gripper is not near " + str(obj)):
        move(obj + " to goal")

# put gripper above the puck
def put(obj):
    if check("the robot's gripper is not vertically aligned with " + str(obj) + " and the robot's gripper is not near " + str(obj)):
