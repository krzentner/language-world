# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper on faucet handle
    #  2. Turn handle left
    #  3. Turn handle left harder until water flows
    # Put gripper on faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper on faucet handle")
    # Turn handle left.
    if check("the robot's gripper is around faucet handle and the handle position is not turned to the left"):
        robot.turn("handle left")
    # If water doesn't flow, turn handle harder until water flows.
    if check("the water is not flowing"):
        robot.turn("handle left harder until water flows")