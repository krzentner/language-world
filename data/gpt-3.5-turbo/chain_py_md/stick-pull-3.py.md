# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Place the gripper above the stick
    #  2. Pick the stick with the gripper
    #  3. Place the stick against the thermos
    #  4. Use the stick to hook onto the thermos handle
    #  5. Pull the thermos to the target location 
    # Place gripper above the stick
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above the stick")
    # Pick up the stick with the gripper
    if check("the stick is not held in the gripper"):
        robot.grab("the stick with the gripper")
    # Place the stick against the thermos
    if check("the stick is not against the thermos and the stick is held in the gripper"):
        robot.place("the stick against the thermos")
    # Use the stick to hook onto the thermos handle
    if check("the stick is against the thermos and the stick is held in the gripper"):
        robot.hook("onto the thermos handle using the stick")
    # Pull the thermos to the target location
    if check("the stick is hooked onto the thermos handle and the thermos is not at the target location"):
        robot.pull("the thermos to the target location using the stick")