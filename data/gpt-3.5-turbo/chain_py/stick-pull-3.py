# Steps:
    #  1. Put gripper above stick near the end we want to use to pull the thermos
    #  2. Grab the stick with the gripper
    #  3. Line the stick up with the thermos
    #  4. Push/pull on the stick to slide the thermos to the goal
    # First, put the gripper in position to grab the stick, near the end we want
    # to use to pull the thermos.
    if check("the robot's gripper is not near the stick and the robot's gripper is not vertically aligned with the stick"):
        robot.move("gripper above stick near pulling end")
    # If the gripper is near the stick but not around it, grab the stick.
    if check("the robot's gripper is near the stick and the robot's gripper is not around the stick"):
        robot.grab("stick")
    # If the gripper is around the stick but the stick isn't lined up with the
    # thermos, line it up.
    if check("the robot's gripper is around stick and the stick is not aligned with the thermos"):
        robot.align("stick to thermos")
    # If the stick is lined up with the thermos, we can use it to slide the
    # thermos to the goal.
    # Push or pull on the stick depending on the orientation of the stick.
    if check("the robot's gripper is around stick and the stick is aligned with thermos"):
        if check("the stick is mostly in front of the thermos"):
            robot.push("thermos towards goal with stick")
        else:
            robot.pull("thermos towards goal with stick")