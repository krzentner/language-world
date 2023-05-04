
    # Steps:
    #  1. Put gripper above mug
    #  2. Grab the mug with the gripper
    #  3. Move mug to goal
    # First, put the gripper above mug, so that we don't bump it while trying to
    # grab it.
    if check("the robot's gripper is not above mug"):
        robot.move_gripper("above mug")
    # If the gripper isn't around mug, put it around mug.
    # To check if the gripper is around mug, check from above.
    # Because we might bump the cup by accident, we want to move to it only if
    # the gripper isn't closed.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("above mug", close_gripper=True)
    # If the gripper is around mug and open, maybe we can grab it by closing the
    # gripper.
    if check("the robot's gripper is around mug and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

# hammer: hit the ball with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above hammer
    #  2. Grab the hammer with the gripper
    #  3. Move the hammer above the ball
    #  4. Drop the hammer on the ball
    # First, put the gripper above hammer, so that we don't bump it while
    # trying to grab it.
    # Because the hammer is a long thin object, check if the gripper is lined up
    # with it from in front instead of around it.
    if check("the robot's gripper is not forward aligned with hammer"):
        robot.move_gripper("above hammer")
    # If the gripper isn't lined up with the hammer, put it around hammer.
    # Because we might bump the hammer by accident, we want to move to it only
    # if the gripper isn't closed.
    if check("the robot's gripper is not around hammer and the robot's gripper is open"):
        robot.move_gripper("below hammer", close_gripper=True)
