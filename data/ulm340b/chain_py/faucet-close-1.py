
    # Steps:
    #  1. Line up the gripper vertically with the faucet handle
    #  2. Grasp the faucet handle with the gripper
    #  3. Turn the faucet handle right
    # First, put the gripper vertically above the faucet handle.
    # We need to do this to make sure that we don't accidentally push the
    # faucet handle up or down while trying to grab it.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # The gripper is vertically aligned, so we can move it around the faucet
    # handle to grab it.
    # We can also close the gripper a little to make sure it grabs.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    # Once the gripper is around the faucet handle, we can turn it right.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet right")

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Line up the gripper vertically with the faucet handle
    #  2. Grasp the faucet handle with the gripper
    #  3. Turn the faucet handle left
    # First, put the gripper vertically above the faucet handle.
    # We need to do this to make sure that we don't accidentally push the
    # faucet handle up or down while trying to grab it.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # The gripper is vertically aligned, so we can move it around the faucet
    # handle to grab it.
    # We can also close the gripper a little to make sure it grabs.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    # Once the gripper is around the faucet handle, we can turn it left.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet left")

#