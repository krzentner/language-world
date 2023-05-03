Here's the code to perform the task:

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper to right of faucet handle")
    if check("the robot's gripper is near the faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")
``` 

This code assumes that the robot is able to turn the faucet handle left to open the faucet. It checks if the gripper is near the faucet handle, grabs the handle, and then turns it left to open the faucet. You may need to adjust the code based on the specific capabilities of your robot and the design of the faucet handle.