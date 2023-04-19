

The steps are:

1. Put gripper above plate
2. Drop gripper around plate
3. Slide plate to the goal

# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Slide plate to the goal
    # First, put the gripper roughly above the plate, so that we don't bump it 
    # while trying to grab it.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper isn't around the plate yet, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is near the plate and open, maybe we can grab it by 
    # closing the gripper.
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    # We closed the gripper, and the plate is still near the gripper, so maybe 
    # we grabbed it.
    # Try to move the plate to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above plate and the robot's gripper is closed"):
        robot.slide("plate to the goal")