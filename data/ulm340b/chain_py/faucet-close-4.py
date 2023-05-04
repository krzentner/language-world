
    # Steps:
    #  1. Put gripper left of the faucet handle
    #  2. Start turning the faucet handle clockwise to close the faucet
    #  3. Turn the faucet harder
    # If the robot's gripper is not lined up with the faucet handle, we should
    # move the gripper near the faucet handle to start pushing.
    if check("the robot's gripper is not vertically aligned with the faucet handle and the robot's gripper is below the faucet handle"):
        robot.put("the gripper above the faucet handle")
    # If the robot's gripper is near the faucet handle we can probably turn the
    # faucet closed now by moving the gripper right.
    if check("the robot's gripper is above the faucet handle and the faucet handle is not right of the robot's gripper"):
        robot.turn("faucet clockwise")
    # If the robot's gripper is starting to be in front of the faucet handle,
    # push harder.
    if check("the robot's gripper is above the faucet handle and the faucet handle is right of the robot's gripper"):
        robot.push("faucet handle to the right")

# plug-side: grab the plug and insert it sideways into the outlet
def plug_side(robot):
    # Steps:
    #  1. Put gripper above the plug
    #  2. Grab the plug with the gripper
    #  3. Line the plug up with the outlet
    #  4. Slide the plug sideways into the outlet
    # First, put the gripper above the plug.
    if check("the robot's gripper is not vertically aligned with the plug"):
        robot.put("gripper above plug")
    # If the plug becomes left of the gripper, go back to putting the gripper
    # above the plug.
    # Because the plug is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plug is not left of the robot's gripper and plug is not forward aligned with the robot's gripper"):
        robot.grab("plug")
    # As long the gripper is still mostly around the plug and the plug isn't
    # lined up with the outlet, line up the plug with the outlet.
    if