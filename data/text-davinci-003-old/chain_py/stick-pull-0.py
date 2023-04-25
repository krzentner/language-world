
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Push the stick against the thermos
    #  4. Pull the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # If the stick is left of the gripper, grab it.
    if check("the stick is not left of the robot's gripper and the robot's gripper is open"):
        robot.grab("stick")
    # If the stick is right of the gripper and the gripper isn't near the
    # thermos, move the stick against the thermos.
    if check("the stick is right of the robot's gripper and the robot's gripper is not near thermos"):
        robot.push("stick against thermos")
    # If the stick is near the thermos, pull the thermos to the goal.
    if check("the stick is near thermos"):
        robot.pull("thermos to goal")