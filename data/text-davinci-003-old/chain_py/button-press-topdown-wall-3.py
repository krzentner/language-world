
    # Steps:
    #  1. Move the robot's gripper to the right of the wall
    #  2. Put the gripper above the button
    #  3. Align the gripper with the button
    #  4. Push down on the button from above
     # We need to move the robot's gripper next to the short wall first.
    if check("the robot's gripper is not to the right of the wall"):
        robot.move("gripper to right of wall")
    # We should now have the gripper above the button.
    if check("the robot's gripper is above the button"):
        robot.put("above button")
    # We should now be able to align the gripper with the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.align("gripper with button")
    # We can now press the button down from above.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# lightswitch-on: turn the light switch on
# def lightswitch_on(robot):
    # Steps:
    #  1. Put gripper above lightswitch
    #  2. Line up gripper with wall switch
    #  3. Push up on lightswitch
    # Put the robot's gripper above the light switch before lining it up with the
    # wall switch.
    if check("the robot's gripper is not vertically aligned with Light switch"):
        robot.put("gripper above light switch")
    # Line up the gripper with the wall switch.
    # Be careful to align the gripper from the front.
    if check("the robot's gripper is not forward aligned with wall switch"):
        robot.align("gripper with wall switch")
    # We should be able to push the light switch up now.
    if check("the robot's gripper is forward aligned with wall switch"):
        robot.push("up on light switch")