
    # Steps:
    #  1. Put gripper on top of plate
    #  2. Push plate back
    #  3. Slide plate right
    # To push the plate back, we need to put the gripper on top of it.
    if check("the robot's gripper is not horizontally aligned with the plate"):
        robot.move("the gripper on top of the plate")
    # Once the gripper is on top of the plate, we can push it back.
    if check("the robot's gripper is horizontally aligned with the plate"):
        robot.push("the plate back")
    # If the gripper is behind the plate, we can move the plate sideways.
    if check("the robot's gripper is behind the plate"):
        robot.slide("the plate right")

# plate-slide-forward-side: slide the plate forward sideways into the target location
def plate_slide_forward_side(robot):
    # Steps:
    #  1. Put gripper on top of plate
    #  2. Push plate forward
    #  3. Slide plate right
    # To push the plate forward, we need to put the gripper on top of it.
    if check("the robot's gripper is not horizontally aligned with the plate"):
        robot.move("the gripper on top of the plate")
    # Once the gripper is on top of the plate, we can push it forward.
    if check("the robot's gripper is horizontally aligned with the plate"):
        robot.push("the plate forward")
    # If the gripper is in front of the plate, we can move the plate sideways.
    if check("the robot's gripper is in front of the plate"):
        robot.slide("the plate right")

# plate-slide-back-topdown: slide the plate back into the target location
def plate_slide_back_topdown(robot):
    # Steps:
    #  1. Put gripper on top of plate
    #  2. Push plate back
    #  3. Slide plate sideways to reach goal
    #  4. Push plate into goal
    # To push the plate back, we need to put the gripper on top of it.
    if check("the robot's gripper is not horizontally aligned with the plate"):
        robot