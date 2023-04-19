

Steps:
1. Put gripper above the plate
2. Drop gripper around the plate
3. Slide the plate towards the target location

```
# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate towards the target location
    # Put the gripper roughly above the plate, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is near the plate and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above plate and the robot's gripper is closed"):
        robot.move_gripper("left of the plate")
    # Once the gripper is lined up above the plate, we should be able to slide
    # it to the target location.
    if check("the robot's gripper is left of the plate"):
        robot.move_gripper("near the target location")