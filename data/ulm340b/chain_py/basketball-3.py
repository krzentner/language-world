
    # Steps:
    #  1. Reach to ball
    #  2. Put gripper around the ball
    #  3. Lift ball to goal
    # First, reach for the ball.
    if check("the robot's gripper is not near the ball"):
        robot.reach("for ball")
    # Once near the ball, grab it
    if check("the robot's gripper is near the ball"):
        robot.close("gripper around the ball")
    # Once grabbed, lift it towards the goal.
    if check("the robot's gripper is around the ball"):
        robot.move("the ball to the goal")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it.
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# pick: pick up the puck
def pick(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    #