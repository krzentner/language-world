

First, put the gripper above the faucet handle.

```
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Turn the faucet handle left
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
```

Once the gripper is vertically aligned with the faucet handle, turn the faucet handle left.

```
    # If the gripper is vertically aligned with the faucet handle, turn the
    # faucet handle left.
    if check("the robot's gripper is vertically aligned with faucet handle"):
        robot.turn("left")
```

Finally, close the block by adding the closing `def` line.

```
    # If the gripper is vertically aligned with the faucet handle, turn the
    # faucet handle left.
    if check("the robot's gripper is vertically aligned with faucet handle"):
        robot.turn("left")

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Turn the faucet handle left
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # If the gripper is vertically aligned with the faucet handle, turn the
    # faucet handle left.
    if check("the robot's gripper is vertically aligned with faucet handle"):
        robot.turn("left")
```