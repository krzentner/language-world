

The robot should: 

1. Put the gripper above the stick
2. Drop the gripper around the stick 
3. Close the gripper around the stick 
4. Move the stick to the target location 
5. Push the thermos with the stick 

```
# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Drop the gripper around the stick
    #  3. Close the gripper around the stick
    #  4. Move the stick to the target location
    #  5. Push the thermos with the stick
    # Put the gripper roughly above the stick, so that we don't bump the thermos
    # while trying to pick up the stick.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper is near the stick and open, try to grab it by closing the
    # gripper.
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # We closed the gripper, and the stick is still near the gripper, so maybe
    # we grabbed it.
    # Try to move the stick to the target location.
    if check("the robot's gripper is above stick and the robot's gripper is closed"):
        robot.place("stick at goal")
    # If the robot's gripper is near the thermos, then use the stick to push the
    # thermos.
    if check("the robot's gripper is near thermos"):
        robot.push("thermos with stick")
```