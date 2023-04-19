

Steps: 
1. Put gripper behind the plate
2. Put gripper around the plate
3. Slide the plate sideways towards the target location

```
# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper behind the plate
    #  2. Put gripper around the plate
    #  3. Slide the plate sideways towards the target location
    # To slide the plate, we need to first move the gripper behind the plate.
    if check("the robot's gripper is not behind the plate"):
        robot.put("gripper behind plate")
    # Move the gripper around the plate.
    if check("the robot's gripper is not around the plate"):
        robot.grab("plate")
    # Now that it's around the plate, we can slide it sideways towards the goal.
    if check("the robot's gripper is around the plate"):
        robot.slide("plate towards goal")
```