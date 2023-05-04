
    # Steps:
    #  1. Put gripper near the mug
    #  2. Grab the mug by closing the gripper
    #  3. Pull the mug to the goal
    # Start by putting the gripper near the mug.
    # This means that the mug is right of the gripper and below the gripper, but
    # we can also put it right above the mug.
    # The mug is small enough that we don't have to be careful of where the
    # gripper is in front of it when putting it above the mug.
    if check("the robot's gripper is not near the mug"):
        robot.move_gripper("above the mug")
    # If the gripper is near the mug but not around it, move the gripper around
    # the mug.
    if check("the robot's gripper is not around mug"):
        robot.move_gripper("around the mug", close_gripper=True)
    # If the gripper is still around the mug, we can pull it to the goal.
    if check("the robot's gripper is below the mug"):
        robot.move_gripper("near the target location")

# coffee-push: grab the mug and push it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper near the mug
    #  2. Grab the mug by closing the gripper
    #  3. Push the mug to the goal
    # Start by putting the gripper near the mug.
    # This means that the mug is left of the gripper and below the gripper, but
    # we can also put it right above the mug.
    # The mug is small enough that we don't have to be careful of where the
    # gripper is in front of it when putting it above the mug.
    if check("the robot's gripper is not near the mug"):
        robot.move_gripper("above the mug")
    # If the gripper is near the mug but not around it, move the gripper around
    # the mug.
    if check("the robot's gripper is not around mug"):
        robot.move_gripper("around the mug", close_gripper=True)
    # If the gripper is still around the mug, we can