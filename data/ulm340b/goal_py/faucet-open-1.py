
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Start turning the faucet handle left
    #  4. Push on the faucet harder
    # Before we can grab the faucet, we need to put the gripper above the faucet
    # handle.
    if check("the robot's gripper is not above faucet handle"):
        robot.move_gripper("above the faucet handle")
    # Once the gripper is above the faucet handle, it should be easy to grab the
    # faucet handle by putting the gripper around it.
    if check("the robot's gripper is not around faucet handle and the robot's gripper is near faucet handle"):
        robot.move_gripper("around the faucet handle")
    # If we've got a good grip on the faucet handle, we can probably start to
    # turn it by moving the gripper left.
    if check("the robot's gripper is around faucet handle"):
        robot.move_gripper("left of the faucet handle")
    # If the faucet is now in front of the gripper, we can push harder to turn
    # it more.
    if check("the robot's gripper is not in front of the faucet handle and the robot's gripper is not left of the faucet handle"):
        robot.move_gripper("horizontally aligned with the faucet handle")

# button-press: push the button
def button_press(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Put gripper around the button
    #  3. Close gripper on button
    #  4. Push down on button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above button"):
        robot.move_gripper("above the button")
    # If the gripper is above the button, put it around the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("around the button")
    # If the gripper is aligned with the button, we might have it surrounded.
    # Close the gripper just in case.
    if check("the robot's gripper is around button