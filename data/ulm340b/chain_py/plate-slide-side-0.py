
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Slide plate to goal
    # First, put the gripper above the plate so that we don't bump it while trying
    # to grab it.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # Put the gripper around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is around the plate, slide it sideways to the target.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.slide("the plate to the goal")

# reacher-v2: reach the target location in the middle of the box
def reacher_v2(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reacher target"):
        robot.reach("to the reacher goal")

# pick-place-wall-v2: pick up the ball and hold it at the target location
def pick_place_wall_v2(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Drop gripper around ball
    #  3. Close gripper around ball
    #  4. Move ball to goal
    # First, put the gripper roughly above ball, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    # If the gripper is near the ball and open, maybe we can grab it by closing
    # the gripper