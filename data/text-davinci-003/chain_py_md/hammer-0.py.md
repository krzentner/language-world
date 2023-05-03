

Then complete the program with the following steps:

1. Put gripper above the hammer
2. Drop gripper around the hammer
3. Close the gripper around the hammer
4. Lift the hammer and swing it down to the nail

Here's the complete program:

```
# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Drop gripper around the hammer
    #  3. Close the gripper around the hammer
    #  4. Lift the hammer and swing it down to the nail
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above hammer")
    # If the gripper isn't around the hammer, put it around the hammer.
    if check("the robot's gripper is not around hammer and the robot's gripper is open"):
        robot.drop("gripper around hammer")
    # If the gripper is near the hammer and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near hammer and the robot's gripper is open"):
        robot.close("gripper around hammer")
    # We closed the gripper, and the hammer is still near the gripper, so maybe we
    # grabbed it.
    # Try to lift the hammer and swing it down to the nail.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above hammer and the robot's gripper is closed"):
        robot.lifting("hammer up")
        robot.swing("from above")