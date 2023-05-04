
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle
    #  3. Pull mug to goal
    # First, we need to put the gripper above the handle before we can grab it.
    # Because the handle is tall, try to align with it from the side, instead of
    # from the top.
    if check("the robot's gripper is not near handle"):
        robot.move("gripper above handle")
    # If the robot's gripper is near the handle, but not aligned from the side,
    # move the gripper to be aligned with the handle.
    if check("the robot's gripper is near handle and the robot's gripper is not sideways aligned with handle"):
        robot.align("gripper to handle")
    # We can grab the handle by moving the gripper sideways towards it.
    if check("the robot's gripper is sideways aligned with handle and the robot's gripper is open"):
        robot.sideways_grab("handle")
    # As long as the gripper is still around the handle, we can pull it to the
    # goal.
    if check("the robot's gripper is around handle"):
        robot.pull("mug to goal")

# coffee-push: push the mug to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Push mug to goal
    # If the mug isn't near the gripper, move the gripper above the mug.
    # We don't need to be careful about the direction, since the mug is large
    # and we're just pushing it (unlike when pulling the mug).
    if check("the robot's gripper is not above mug"):
        robot.move("gripper above mug")
    # Now that the gripper is above the mug, we can try to push it towards the
    # target location.
    if check("the robot's gripper is above mug"):
        robot.push("mug to goal")

# block-regrasp-side: pick up the block and hold it at the target location
def block_regrasp_side(robot):
    # Steps:
    #  1. Put gripper above block
    #  