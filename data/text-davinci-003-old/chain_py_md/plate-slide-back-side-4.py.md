

Then write the code using the techniques you've seen above:

```
# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps:
    #  1. Move gripper left of the plate
    #  2. Trap the plate with the gripper
    #  3. Slide the plate back into the target location
    # First, move the robot's gripper left of the plate. 
    if check("the robot's gripper is not left of the plate"):
        robot.move("gripper to the left of the plate")
    # If the gripper is left of the plate, try to grab the plate. 
    if check("the robot's gripper is left of the plate and the robot's gripper is open"):
        robot.grab("plate with the gripper")
    # If the gripper is around the plate, we can slide it back into the goal. 
    if check("the robot's gripper is around the plate and the robot's gripper is closed"):
        robot.slide("plate into goal")
```