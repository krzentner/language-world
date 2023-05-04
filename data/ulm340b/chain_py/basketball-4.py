
    # Steps:
    #  1. Put gripper above the ball
    #  2. Drop gripper around ball
    #  3. Close gripper around ball
    #  4. Put gripper above the hoop
    #  5. Drop ball into hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.put("gripper above ball")
    # If the ball isn't around the gripper, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    # If the gripper is around the ball and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is around ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # We closed the gripper, and the ball is still near the gripper, so maybe we
    # grabbed it.
    # Put the ball above the hoop.
    if check("the robot's gripper is near ball"):
        robot.put("gripper above hoop")
    # The ball is above the hoop and near the gripper, so just drop the ball
    # into the hoop.
    if check("the robot's gripper is near ball"):
        robot.drop("ball into hoop")

# pick-place-wall: grab the puck and place it on top of the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Drop gripper around the puck
    #  3. Close the gripper around the puck
    #  4. Put gripper above the goal
    #  5. Drop the puck
    # Put the gripper above the puck, since it's small and we don't want to
    # knock it out of the way.
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's grip