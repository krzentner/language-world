

Then, write the rest of the function to demonstrate how the robot can open the faucet.

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper left of the faucet handle
    #  2. Start turning the faucet handle left
    #  3. Push the faucet handle harder
    # First, move the gripper just to the left of the faucet handle.
    if check("the robot's gripper is not left of the faucet handle"):
        robot.move_gripper("left of the faucet handle")
    # If the robot's gripper is left of the handle we can start turning it.
    # Start by turning the handle slowly, so we don't break it.
    if check("the robot's gripper is left of the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # As long as the handle isn't fully open, push it a little harder.
    if check("the robot's gripper is around the faucet handle and the faucet is not fully open"):
        robot.move_gripper("further around the faucet handle")
```