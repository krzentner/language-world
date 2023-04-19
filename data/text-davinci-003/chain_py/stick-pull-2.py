
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Pull the stick towards the robot
    #  4. Move the robot so that the stick is pushing the thermos
    #  5. Push the stick to move thermos to the goal
    # Move the gripper above the stick.
    if check("the robot's gripper is not above stick"):
        robot.put('gripper above stick')
    # Put the gripper around the stick if it's not already.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.grab('stick')
    # Pull the stick towards us, so it's in a position to push the thermos.
    if check("the robot's gripper is not pushing against the thermos and the robot's gripper is around the stick"):
        robot.pull("stick towards robot")
    # Move the robot towards the goal while pushing the stick to move the
    # thermos as well.
    if check("the robot's gripper is pushing against the thermos and stick is reaching toward the target location"):
        robot.push("stick so that the thermos is moved to the target location")