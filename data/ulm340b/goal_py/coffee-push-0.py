
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Put gripper around mug handle
    #  3. Push the mug to the goal location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not above mug handle and the robot's gripper is not vertically aligned with mug handle"):
        robot.move_gripper("above mug handle")
    # Once the gripper is above the mug handle, put it around the handle.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.move_gripper("around mug handle")
    # Once the gripper is around the handle, we can just push the mug to the
    # target location.
    if check("the robot's gripper is around mug handle and the robot's gripper is below mug handle"):
        robot.move_gripper("vertically aligned with mug handle")

# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Put gripper around mug handle
    #  3. Pull the mug to the goal location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not above mug handle and the robot's gripper is not vertically aligned with mug handle"):
        robot.move_gripper("above mug handle")
    # Once the gripper is above the mug handle, put it around the handle.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.move_gripper("around mug handle")
    # Once the gripper is around the handle, we can just pull the mug to the
    # target location.
    if check("the robot's gripper is around mug handle and the robot's gripper is below mug handle"):
        robot.move_gripper("vertically aligned with mug handle")

# coffee-lift: pick up the mug and hold it above the target location
def coffee_lift(robot):
    # Steps:
    #  1. Put gripper above mug handle
    #  2.