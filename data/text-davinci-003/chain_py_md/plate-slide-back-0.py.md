

The program should do the following steps:

1. Put gripper above plate.
2. Drop gripper around plate.
3. Push the plate back to its target location.

```
# plate-slide-back: slide the plate back into the target location
# def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Push the plate back to its target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.put("gripper above plate")
    # If the plate is beneath the gripper as seen from above, line the gripper up 
    # around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is vertically aligned with plate"):
        robot.drop("gripper around plate")
    # Once the gripper is around the plate, we can just push it back to its target
    # location.
    if check("the robot's gripper is around plate"):
        robot.push("plate back to target")
```