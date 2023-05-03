```
# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the edge of the plate
    #  3. Close gripper around the edge of the plate
    #  4. Move the plate to the target location
    # First, put the gripper roughly above the plate so we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # Once the gripper is above the plate, we can drop it around the edge of
    # the plate and close the gripper to hold onto it.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the edge of the plate"):
        robot.move_gripper("around the edge of the plate", close_gripper=True)
    # Finally, we can move the plate to the target location by sliding it
    # while keeping the gripper around the edge of the plate for control.
    if check("the robot's gripper is around the edge of the plate and the plate is not at the target location"):
        robot.move_gripper("above the target location")
```