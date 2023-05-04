
    # Steps:
    #  1. Put gripper above plate
    #  2. Put gripper on plate
    #  3. Push plate sideways to the goal
    # Put the gripper above the plate.
    if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    # Put the gripper on top of the plate
    if check("the robot's gripper is above plate and the robot's gripper is not on plate"):
        robot.place("gripper on plate")
    # We're now on top of the plate, and the gripper is still there, so we can
    # probably slide it to the goal.
    if check("the robot's gripper is on plate and the robot's gripper is above plate"):
        robot.slide("plate to the goal")

# plate-slide-topdown: slide the plate forward into the target location
def plate_slide_topdown(robot):
    # Steps:
    #  1. Put gripper in front of the plate
    #  2. Put gripper on plate
    #  3. Push plate forward to the goal
    # Put the gripper in front of the plate
    if check("the robot's gripper is not in front of plate"):
        robot.put("gripper in front of plate")
    # Put the gripper on top of the plate
    if check("the robot's gripper is in front of plate and the robot's gripper is not on plate"):
        robot.put("gripper on plate")
    # Push the plate forward into the goal
    if check("the robot's gripper is on plate and the robot's gripper is in front of plate"):
        robot.push("plate towards goal")

# plate-grasp-side: grasp the plate and move it to the target location
def plate_grasp_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate
    #  3. Lift plate to goal
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # Put the gripper around the plate.