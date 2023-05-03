
    # Steps:
    #  1. Grab the stick with the robot's gripper
    #  2. Push the stick against the thermos
    #  3. Pull the thermos by pushing the stick away
    # We need to grab the stick with the robot's gripper before we can use it to
    # push the thermos.
    # And if the the stick isn't to the right of the gripper, move the gripper
    # to the stick.
    if check("the stick is not to the right of the robot's gripper and the robot's gripper is not near the stick"):
        robot.grab("stick")
    # Once the gripper is near the stick, line it up with the stick.
    if check("the robot's gripper is near the stick and the robot's gripper is not forward aligned with the stick"):
        robot.move("the gripper forward aligned with the stick")
    # Now that the gripper and stick are lined up, slide the stick against the
    # thermos.
    if check("the robot's gripper is forward aligned with the stick and the thermos is not near the stick"):
        robot.slide("stick near thermos")
    # If the thermos is near the stick, but not close to goal, lift the stick up
    # and push the thermos away from the stick towards the goal.
    if check("the thermos is near the stick and the thermos is not close to goal"):
        robot.push("away from thermos towards goal")