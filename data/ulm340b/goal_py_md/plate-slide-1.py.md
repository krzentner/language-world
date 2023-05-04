

When you are finished, write `DONE` here.

ANSWER:
# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Move gripper above the plate
    #  2. Close gripper around the plate
    #  3. Move plate to target location
    # First, put the gripper roughly above plate, so that we don't bump it while trying to grab it.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("vertically aligned with the plate", close_gripper=True)
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is near the plate and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is around plate and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
DONE


Q3: The robot also needs to perform the `reach` task:

```
# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")
```

But this won't work in its current form. Please fix it so that the robot moves to the `reach target`.

When you are finished, write `DONE` here.

ANSWER:
# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near reach target")
DONE


Q4: The robot's program must be careful about how the robot interacts with objects, because sometimes the robot can push objects out of position or drop objects it's holding. Please fix the bug in the following code so that the robot doesn't drop the plate.

```
# plate-slide: slide the plate into the target location
def plate_slide(robot):
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("vertically aligned with the plate", close_gripper=True)
   