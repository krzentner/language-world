```
# plate-slide-back: slide the plate back into the target location
# def plate_slide_back(robot):
    # Steps:
    #  1. Move gripper above plate
    #  2. Push gripper down onto plate
    #  3. Slide plate back to goal
    # First, put the gripper above the plate
    if check("the robot's gripper is not above the plate"):
        robot.reach("to plate")
    # If the gripper is not touching the plate, move the gripper down onto it.
    if check("the robot's gripper is not touching the plate"):
        robot.push("the gripper onto the plate")
    # If the gripper is touching the plate, slide the plate back
    if check("the robot's gripper is touching the plate and the plate is in front of the robot's gripper"):
        robot.slide("the plate back to the goal")