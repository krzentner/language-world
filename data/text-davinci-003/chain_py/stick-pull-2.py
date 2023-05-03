
    # Steps:
    #  1. Put gripper above stick
    #  2. Grab stick with gripper
    #  3. Pull stick to tug the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.place("gripper above the stick")
    # If the stick becomes left of the gripper, go back to putting the gripper
    # above the stick.
    # Because the stick is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the stick is not left of the robot's gripper and the stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    # As long the gripper is still almost around the stick and the stick isn't
    # lined up with the goal, line up the stick with the goal.
    if check("the robot's gripper is forward aligned with the stick and thestick is not pointing towards the goal"):
        robot.align("stick towards goal")
    # If the stick is lined up with the goal, pull the stick to the side. Pulling
    # the stick should tug the thermos to the goal.
    if check("the stick is pointing towards the goal"):
        robot.pull("stick to goal")