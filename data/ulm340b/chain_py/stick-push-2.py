
    # Steps:
    #  1. Put gripper above the stick
    #  2. Put gripper around the stick
    #  3. Put gripper behind the thermos
    #  4. Push the thermos forward
    # Because the stick is thin, we can't use the "put gripper near stick"
    # approach we use for other objects.
    # Instead, we'll use a "put gripper above object and drop gripper around
    # object" approach.
    # If the gripper is not above the stick, place it above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # Now that the gripper is above the stick, maybe we can grab the stick.
    if check("the robot's gripper is above stick and the robot's gripper is not around stick"):
        robot.drop("gripper around stick")
    # Now that we have the stick, we'll try pushing the thermos to the goal.
    # First, put the gripper behind the thermos.
    if check("the robot's gripper is below the stick"):
        robot.place("gripper above thermos")
    if check("the robot's gripper is above thermos"):
        robot.place("gripper behind thermos")
    # Now that the gripper is behind the thermos, maybe we can push the thermos
    # to the goal.
    if check("the robot's gripper is behind thermos"):
        robot.push("thermos to goal")

# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Put gripper around the stick
    #  3. Pull the thermos to goal
    # Because the stick is thin, we can't use the "put gripper near stick"
    # approach we use for other objects.
    # Instead, we'll use a "put gripper above object and drop gripper around
    # object" approach.
    # If the gripper is not above the stick, place it above the stick.
    if check("the robot's gripper is not above