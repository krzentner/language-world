
    # Steps:
    #  1. Put gripper above the stick
    #  2. Drop gripper around the stick
    #  3. Put gripper near the thermos
    #  4. Use the stick to push the thermos to the target location
    # To start, we need to pick up the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # Now that the gripper is near the stick, we need to drop it onto the stick.
    if check("the robot's gripper is above the stick"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is around the stick, we can now use it to push the thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("near the thermos", close_gripper=True)
    # Move the gripper to push the thermos to the target location.
    if check("the robot's gripper is near the thermos"):
        robot.move_gripper("near the target location")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab