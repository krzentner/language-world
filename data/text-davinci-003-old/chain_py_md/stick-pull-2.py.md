

To complete the task:
    1. Put the gripper above the stick
    2. Put the gripper around the stick
    3. Pull the stick away from the thermos
    4. Move the stick to the target location
    5. Put the gripper above the thermos
    6. Move the gripper to the target location

```
# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Put the gripper around the stick
    #  3. Pull the stick away from the thermos
    #  4. Move the stick to the target location
    #  5. Put the gripper above the thermos
    #  6. Move the gripper to the target location
    # First, put the gripper above the stick so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the stick is near the gripper and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # We closed the gripper, and the stick is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the stick away from the thermos.
    # If we didn't grab it, we'll just go back to an earlier step. 
    if check("the robot's gripper is above the stick and the robot's gripper is closed"):
        robot.pull("stick away from the thermos")
    # If the stick is away from the thermos, move the stick to the target location.
    if check("the robot's gripper is above the stick which is away from thermos"):
        robot.move("stick to the target location")
    # After the stick is at the target location, put the gripper above the thermos.
    if check("the robot's gripper is above the stick and the stick is at the target location"):
        robot.put("gripper above the thermos")
    # If the thermos is below the gripper, try to