

Then write the functions to perform the task.

# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push the plate across the table
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the plate is left of the robot's gripper, start pushing the plate.
    if check("the robot's gripper is above the plate and the plate is not left of the robot's gripper"):
        robot.move_gripper("left of the plate")
    # If the plate is left of the robot's gripper and the robot's gripper is 
    # starting to be near the plate, start pushing it.
    if check("the robot's gripper is almost near the plate"):
        robot.move_gripper("left of the plate")
    # Once the gripper is near the plate, start pushing it to the target 
    # location.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("above the target location")