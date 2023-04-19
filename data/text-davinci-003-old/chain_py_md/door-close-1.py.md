

Then, write the steps: 

```
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push door closed
    # First, put the gripper roughly above door handle, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the door handle"):
        robot.put("gripper above door handle")
    # If the gripper isn't around the door handle, put it around the door handle.
    if check("the robot's gripper is not around door handle and the robot's gripper is open"):
        robot.drop("gripper around door handle")
    # If the gripper is near the door handle and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near door handle and the robot's gripper is open"):
        robot.close("gripper around door handle")
    # We closed the gripper, and the door handle is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the door to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above door handle and the robot's gripper is closed"):
        robot.place("door at goal")
```