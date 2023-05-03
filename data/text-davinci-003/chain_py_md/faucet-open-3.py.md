

Then provide the steps as code:

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps: 
    #  1. Put gripore above the faucet
    #  2. Drop gripper around the faucet handle
    #  3. Turn the faucet left
    
    # Move the gripper above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"): 
        robot.put("gripper above the faucet handle")
    # Put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle and the robot's gripper is open"):
        robot.drop("gripper around the faucet handle")
    # When the gripper is around the faucet handle, start turning the faucet left.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")
```