

and add code to solve the task.

# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Move gripper around the plate
    #  3. Slide the plate to destination
    # Place the robot's gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, move it near the plate.
    if check("the robot's gripper is not around plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is around the plate, slide it to the target location.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("above the target location")