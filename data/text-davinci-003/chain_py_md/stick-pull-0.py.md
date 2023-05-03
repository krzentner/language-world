

# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Close the gripper around the stick 
    #  3. Lower the gripper around the stick 
    #  4. Push the gripper towards the thermos
    #  5. Pull the thermos to the target location
    # First, put the gripper above the stick
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # If the gripper is near the stick, close it.
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # If the gripper is closed around the stick and the stick is not lowered,
    # start lowering the gripper around the stick.
    if check("the robot's gripper is closed around the stick and the stick is not lowered"):
        robot.lower("gripper around stick")
    # Now that the stick is lowered, we can push the gripper towards the thermos.
    if check("the robot's gripper is closed around the stick and the stick is lowered"):
        robot.push("gripper towards thermos")
    # If the gripper is near the thermos, start pulling it to the target location.
    if check("the robot's gripper is near the thermos"):
        robot.pull("thermos to the target location")