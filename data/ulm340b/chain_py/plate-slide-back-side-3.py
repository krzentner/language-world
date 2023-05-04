
    # Steps:
    #  1. Put gripper right of plate
    #  2. Start pushing on the plate
    #  3. Push harder to slide the plate to the goal
    # If the gripper is not in front of the plate, move it there.
    if check("the plate is in front of the robot's gripper"):
        robot.grab("plate")
    # If the plate is still in front of the gripper, try sliding it to the
    # goal.
    if check("the robot's gripper is near the plate"):
        robot.push("plate to goal")

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper right of plate
    #  2. Start pushing on the plate
    #  3. Push harder to slide the plate to the goal
    # If the gripper is not in front of the plate, move it there.
    if check("the plate is in front of the robot's gripper"):
        robot.grab("plate")
    # If the plate is still in front of the gripper, try sliding it to the
    # goal.
    if check("the robot's gripper is near the plate"):
        robot.push("plate to goal")

# plate-slide-back: slide the plate backwards into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper right of plate
    #  2. Start pushing on the plate
    #  3. Push harder to slide the plate to the goal
    # If the gripper is not in front of the plate, move it there.
    if check("the plate is in front of the robot's gripper"):
        robot.grab("plate")
    # If the plate is still in front of the gripper, try sliding it to the
    # goal.
    if check("the robot's gripper is near the plate"):
        robot.push("plate to goal")

# block-pick-place: pick up the block and hold it at the target location
def block_pick_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2.