

# dial-turn: turn the dial
def dial_turn(robot):
    # Steps: 
    #  1. Put gripper above dial 
    #  2. Grab dial with gripper
    #  3. Turn dial to goal
    # First, put the gripper above the dial as seen from the top, to make sure
    # we don't bump it while trying to grab it.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    # Once the gripper is lined up above the dial, we should be able to grab
    # the dial by moving the gripper around it.
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not around dial"):
        robot.grab("dial")
    # If the gripper is near the dial and it's closed, maybe we can turn it to
    # the goal by pushing the gripper.
    if check("the robot's gripper is near dial and the robot's gripper is closed"):
        robot.turn("dial to goal")