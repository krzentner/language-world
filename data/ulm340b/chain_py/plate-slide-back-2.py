
    # Steps:
    #  1. Put gripper in front of the plate
    #  2. Slide the plate back
    #  3. Push the plate back harder
    # If the robot's gripper isn't near the plate, we should move it in front of
    # the plate so we can push it back.
    if check("the plate is not near the robot's gripper"):
        robot.put("gripper in front of plate")
    # If the gripper is in front of the plate, we should start pushing it back.
    if check("the plate is near the robot's gripper"):
        robot.slide("plate back")
    # If the gripper is now more above the plate than in front of the plate,
    # slide it back harder.
    if check("the robot's gripper is vertically aligned with plate"):
        robot.push("plate back harder")

# plate-slide: slide the plate to the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper in front of the plate
    #  2. Slide the plate forward
    #  3. Push the plate forward harder
    # If the robot's gripper isn't near the plate, we should move it in front of
    # the plate so we can push it.
    if check("the plate is not near the robot's gripper"):
        robot.put("gripper in front of plate")
    # If the gripper is in front of the plate, we should start pushing it
    # forward.
    if check("the plate is near the robot's gripper"):
        robot.slide("plate forward")
    # If the gripper is now more above the plate than in front of the plate,
    # slide it forward harder.
    if check("the robot's gripper is vertically aligned with plate"):
        robot.push("plate forward harder")

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper near the plate
    #  2. Slide the plate sideways
    #  3. Push the plate sideways harder
    # If the robot's gripper isn't near the plate, we should move it in