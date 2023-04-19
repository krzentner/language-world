

# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Place the stick at the robot's side with the end facing the thermos
    #  3. Retract the stick with the gripper until the stick is at the back of the thermos
    #  4. Push the thermos to the goal
    # First, bring the gripper near the stick.
    if check("the robot's gripper is not near the stick"):
        robot.put("gripper above stick")
    # Move the stick to the robot's side so that the end of the stick points
    # toward the thermos
    if check("stick is not at the side of the robot"):
        robot.place("stick to the side")
    # Pull the stick back with the gripper until the stick is at the back of
    # the thermos
    if check("stick is not at the back of the thermos"):
        robot.pull("stick back")
    # The stick is now positioned to push the thermos.
    # Push the thermos forward.
    if check("stick is at the back of the thermos and the robot's gripper is near the stick"):
        robot.push("thermos to goal")