
    # Steps:
    #  1. Put gripper above stick
    #  2. Grab the stick with the gripper
    #  3. Move the stick to the thermos
    #  4. Push the thermos with the stick
    # We want to use the stick to move the thermos, so the first step is to pick
    # up the stick.
    # Put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # If the stick becomes left of the gripper, go back to putting the gripper
    # above the stick and pick it up with the gripper.
    # Because the stick is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    # If the stick is near the thermos from a side view, we can push against it,
    # so push the stick against the thermos.
    if check("the robot's gripper is forward aligned with the stick and the stick is near the side of the thermos"):
        robot.push("stick against thermos")
    # If the stick is pushing against the thermos, push harder.
    if check("the stick is pushing against the thermos"):
        robot.push("stick against thermos harder")