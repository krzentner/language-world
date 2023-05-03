# Steps:
    # 1. Put the gripper above the puck
    # 2. Drop the gripper around the puck
    # 3. Close the gripper around the puck
    # 4. Move the gripper and puck to the goal location
    # The robot needs to pick up the puck manually without any arm movement.
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, we can grab it by closing the
    # gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, so we probably grabbed the puck.
    # We need to manually move the gripper and the puck to the goal location.
    # Because this is a manual movement, we don't have any specific steps to
    # follow, so we'll just assume the human operator knows what they're doing.
    # Once the gripper and the puck are at the goal location, we can release the
    # puck.
    if check("the gripper and puck are at the goal location"):
        robot.release("puck")