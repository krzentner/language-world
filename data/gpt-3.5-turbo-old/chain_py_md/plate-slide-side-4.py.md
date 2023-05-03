```
# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate towards the target while keeping it level
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper is not around the plate, grab it with the gripper.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is near the plate and closed, move the plate to the target
    # location while keeping it level.
    if check("the robot's gripper is near plate and the robot's gripper is closed"):
        robot.slide("plate towards target while keeping it level")
```