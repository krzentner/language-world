
    # Steps:
    #  1. Put gripper above lid
    #  2. Pick up the lid
    #  3. Align the lid with the box
    #  4. Place the lid on the box
    # First, put the gripper roughly above the lid.
    if check("the robot's gripper is not above the lid"):
        robot.move_gripper("above the lid")
    # From here, make sure the gripper is around the lid.
    # Close the gripper to make sure it gets grasped.
    if check("the robot's gripper is not around lid"):
        robot.move_gripper("around the lid", close_gripper=True)
    # If the lid is left of the gripper and the gripper is closed, we should
    # move the gripper back to the box with the lid grasped.
    if check("the lid is left of the robot's gripper and the robot's gripper is closed"):
        robot.move_gripper("above the box")
    # Now that the gripper is above the box and the lid is inside it, line up the
    # lid with the box.
    if check("the robot's gripper is above box and lid is horizontally aligned with box"):
        robot.move_gripper("horizontally aligned with box")

# cup-pickuplace: pick up the cup, rotate it, and place it down
def cup_pickuplace(robot):
    # Steps:
    #  1. Put gripper above the cup
    #  2. Grab the cup with the gripper
    #  3. Rotate the cup
    #  4. Place the cup down
    # First, drop the gripper above the cup to avoid bumping it while trying to
    # grab it.
    if check("the robot's gripper is not above the cup"):
        robot.move_gripper("above the cup")
    # If the cup is left of the gripper, move the gripper around it and close
    # the gripper.
    if check("the robot's gripper is not near cup and the robot's gripper is open"):
        robot.move_gripper("near the cup", close_gripper=True)
    # If the cup is near the robot's gripper and closed, start rotating it.
    if check("the robot's gripper is closed and the robot's gripper is near cup"):
        robot.move_gripper("rotating the cup")
    # Once the cup has been rotated, move it to the goal to place it down.