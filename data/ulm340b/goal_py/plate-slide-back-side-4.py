
    # Steps:
    #  1. Line up gripper with plate
    #  2. Line up plate with goal
    #  3. Push plate into the goal
    # First, line up the gripper with the plate.
    if check("the robot's gripper is not horizontally aligned with plate"):
        robot.move_gripper("horizontally aligned with plate")
    # Next, push the plate into the goal if the plate is lined up with the goal.
    if check("plate is horizontally aligned with goal"):
        robot.move_gripper("vertically aligned with plate")

# plate-slide-forward-side: slide the plate forward sideways into the target location
def plate_slide_forward_side(robot):
    # Steps:
    #  1. Line up gripper with plate
    #  2. Line up plate with goal
    #  3. Push plate into the goal
    # First, line up the gripper with the plate.
    if check("the robot's gripper is not horizontally aligned with plate"):
        robot.move_gripper("horizontally aligned with plate")
    # Next, push the plate into the goal if the plate is lined up with the goal.
    if check("plate is horizontally aligned with goal"):
        robot.move_gripper("vertically aligned with plate")

# door-unlock-side: turn the key counter-clockwise to unlock the door
def door_unlock_side(robot):
    # Steps:
    #  1. Put gripper around key
    #  2. Turn the key counter-clockwise
    # First, put the gripper around the key.
    if check("the robot's gripper is not around key"):
        robot.move_gripper("vertically aligned with key")
    # Now that the gripper is lined up with the key, we can just turn the key.
    if check("the robot's gripper is around key"):
        robot.move_gripper("horizontally aligned with key")

# door-lock-side: turn the key clockwise to lock the door
def door_lock_side(robot):
    # Steps:
    #  1. Put gripper around key
    #  2. Turn the key clockwise
    # First, put the gripper around the key.
    if check("the robot's