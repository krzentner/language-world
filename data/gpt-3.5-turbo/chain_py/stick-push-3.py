# Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Move the gripper to the side of the thermos
    #  4. Use the stick to push the thermos to the goal
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # If the gripper is above the stick, but not grabbing it, grab it.
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.grab("stick")
    # If we're holding the stick, move the gripper to the side of the thermos.
    # We want to be careful to not accidentally push the thermos over.
    if check("the robot's gripper is holding the stick and the thermos is not near the stick's end and the thermos is not between the stick and the robot"):
        robot.move("gripper near thermos without hitting it")
    # If the gripper is close to the thermos, start using the stick to push it.
    if check("the robot's gripper is near the thermos and the stick is angled towards the thermos"):
        robot.push("stick against the thermos towards the goal")