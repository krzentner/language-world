```
# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Put the end of the stick near the thermos
    #  4. Push the thermos to the goal using the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.drop("gripper around the stick")
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the stick and the robot's gripper is open"):
        robot.close("gripper around the stick")
    # We closed the gripper, and the stick is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the stick near the thermos.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above the stick and the robot's gripper is closed and the stick is not next to the thermos"):
        robot.reach("to the thermos")
    # Once the stick is near the thermos, use it to push the thermos.
    if check("the stick is next to the thermos"):
        robot.push("thermos to the goal using the stick")
```