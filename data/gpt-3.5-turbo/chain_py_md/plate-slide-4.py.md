# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Slide plate to goal
    # First, put the gripper roughly above the plate.
    if check("the robot's gripper is not above plate"):
        robot.place("gripper above plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is near the plate and open, we can slide the plate by moving
    # the gripper.
    # Close the gripper to make sure we keep control of the plate.
    if check("the robot's gripper is near plate and the plate is below the robot's gripper"):
        robot.slide("the plate to the goal")