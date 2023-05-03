

Then add the following code to the function:

```
    # Steps:
    #  1. Put gripper to the left of the plate
    #  2. Move the gripper to the right side of the plate such that it traps the plate 
    #  3. Slide the plate sideways into the target location
    # First, move the gripper to the left of the plate.
    if check("the robot's gripper is not left of the plate"):
        robot.move_gripper("left of the plate")
    # If the plate is left of the gripper, go back to putting the gripper
    # left of the plate
    # because the plate is a flat object, check if the gripper is lined up with it
    # from the front instead of from the side.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate")
    # As long the gripper is still to the left of the plate, move it next to
    # the plate.
    if check("the robot's gripper is to the left of the plate"):
        robot.move_gripper("right of the plate")
    # If the plate is now to the left of the gripper, we can slide the plate
    # sideways into the target location.
    if check("the robot's gripper is right of the plate"):
        robot.move_gripper("horizontally aligned with the target location")
```