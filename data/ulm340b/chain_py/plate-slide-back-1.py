
    # Steps:
    #  1. Put gripper near plate
    #  2. Push plate forward
    #  3. Keep pushing plate forward
    # Since the plate is fairly flat and large, all we need to do is push on it
    # to move it.
    if check("the robot's gripper is not near plate"):
        robot.move("gripper near plate")
    # If the gripper is near the plate, push the plate forward by moving the
    # gripper forward.
    if check("the robot's gripper is near plate and the gripper is forward aligned with plate"):
        robot.slide("plate forward")
    # As long as the gripper is aligned with the plate, keep pushing it forward.
    if check("the robot's gripper is forward aligned with plate"):
        robot.push("plate forward")

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper near plate
    #  2. Push plate left
    #  3. Keep pushing plate left
    # Since the plate is fairly flat and large, all we need to do is push on it
    # to move it.
    if check("the robot's gripper is not near plate"):
        robot.move("gripper near plate")
    # If the gripper is near the plate, push the plate sideways by moving the
    # gripper sideways.
    if check("the robot's gripper is near plate and the gripper is forward aligned with plate"):
        robot.slide("plate left")
    # As long as the gripper is aligned with the plate, keep pushing it sideways.
    if check("the robot's gripper is forward aligned with plate"):
        robot.push("plate left")

# plate-width-slide-side: slide the plate sideways to the left
def plate_width_slide_side(robot):
    # Steps:
    #  1. Put gripper near plate
    #  2. Push plate left
    #  3. Keep pushing plate left
    # Since the plate is fairly flat and large, all we need to do is push on it
    # to move it.
    if check("the robot's gripper is not