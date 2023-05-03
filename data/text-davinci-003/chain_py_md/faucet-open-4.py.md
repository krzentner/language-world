

The program should be a series of steps to instruct the robot to open a faucet by turning it left.

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Grab the handle with the gripper
    #  3. Turn the handle left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # If the gripper is still mostly around the faucet handle, go ahead and grab
    # it.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is open"):
        robot.grab("faucet handle")
    # As long as the faucet handle is still in the same position, keep turning
    # left.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is closed"):
        robot.turn("faucet handle left")