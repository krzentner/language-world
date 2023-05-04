
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Pull mug to goal
    # First, put the gripper above the mug handle so we don't accidentally knock
    # the mug over.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.put("gripper above mug handle")
    # Once the gripper is roughly above the mug handle, we can lower the gripper
    # down around the handle to pick it up.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.drop("gripper around mug handle")
    # If the mug handle is roughly in front of the gripper, pull the mug handle
    # forward.
    if check("the robot's gripper is roughly forward aligned with mug handle"):
        robot.pull("mug to goal")

# coffee-push: push the mug to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Push mug to goal
    # First, put the gripper above the mug handle so we don't accidentally knock
    # the mug over.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.put("gripper above mug handle")
    # Once the gripper is roughly above the mug handle, we can lower the gripper
    # down around the handle to pick it up.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.drop("gripper around mug handle")
    # If the mug handle is roughly in front of the gripper, push the mug forward.
    if check("the robot's gripper is roughly forward aligned with mug handle"):
        robot.push("mug to goal")

# button-press: press the button
def button_press(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Drop gripper around button
    #  3. Push the button
    #