

Here's the code:
```
# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Line up the gripper with faucet
    #  2. Grab the faucet handle
    #  3. Turn the faucet left
    # First, line up the robot's gripper with the faucet handle.
    if check("the robot's gripper is not horizontally aligned with faucet handle"):
        robot.put("gripper next to faucet handle")
    # If the gripper is lined up, we can grab the faucet handle.
    if check("the robot's gripper is horizontally aligned with the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # Now that the gripper is around the faucet handle, we can turn the faucet
    # left.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")
```