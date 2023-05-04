
    # Steps:
    #  1. Put gripper above handle
    #  2. Put gripper around handle
    #  3. Pull up on handle
    #  4. Pull up harder on handle
    # First, we need to put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # If the robot's gripper is vertically aligned with the handle, we should be
    # able to grab it by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.put("gripper around handle")
    # As long as the robot's gripper is around the handle and not in front of it
    # we can pull it up.
    if check("the robot's gripper is around handle and the robot's gripper is not in front of handle"):
        robot.pull("handle up")
    # If the robot's gripper is in front of the handle, pull harder to pull it
    # up more.
    if check("the robot's gripper is in front of handle"):
        robot.pull("handle up harder")

# button-press-side: slide the button horizontally along the table
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Line up gripper to press button from the side
    #  3. Move gripper toward button to push it
    #  4. Move gripper toward button to push it harder
    # First, we need to put the gripper above the button.
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    # If the robot's gripper is above the button and forward aligned with the
    # button, line up the gripper to the side of the button so it can push it
    # toward the table.
    if check("the robot's gripper is above button and the robot's gripper is forward aligned with button"):
        robot.align("gripper to the side of button")
    # If the gripper is lined up next to the button, push the button by moving
