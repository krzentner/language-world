
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Grab the handle with the gripper
    #  3. Turn the faucet left
    # To turn on the faucet, we first have to put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle", close_gripper=True)
    # Now that the gripper is lined up, grab the handle with the gripper.
    if check("the robot's gripper is vertically aligned with the faucet handle"):
        robot.move_gripper("left of the faucet handle")
    # If the gripper is in front of the handle and the handle is not open, turn
    # the handle left.
    if check("the robot's gripper is forward aligned with faucet handle"):
        robot.move_gripper("left of the faucet handle")

# detect-clothing: detect clothing items in a photo
def detect_clothing(robot):
    # Steps:
    #  1. Take a photo
    #  2. Use AI to detect clothing items in the photo
    # Taking a photo is an external step that the robot will not perform.
    # We can just assume that a photo has been taken and use AI to detect the
    # clothing items in the photo.
    if check("there is a photo"):
        robot.detect_clothing()