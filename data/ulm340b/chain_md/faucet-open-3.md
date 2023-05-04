
    Steps:  1. Turn the faucet left
    You don't have to turn the faucet gently, so you can just turn it left.
    - When faucet is closed, the robot should turn faucet left.

The task `faucet-close` requires the robot to turn the faucet right.
To turn the faucet right reliably, what steps the robot should perform?
    Steps:  1. Turn the faucet right
    You don't have to turn the faucet gently, so you can just turn it right.
    - When faucet is open, the robot should turn faucet right.

The task `push-hard` requires the robot to slide the window to the right more firmly.
To slide the window to the right more firmly reliably, the robot should perform the following steps:
    Steps:  1. Put gripper left of the window handle  2. Slide the window right  3. Push the window closed harder
    We're pushing the window hard, so it's okay if the gripper is not aligned with it from the front.
    - When the robot's gripper is not near the window handle and the robot's gripper is left of window handle, the robot should move gripper to left of window handle.
    If the gripper is left of the window handle, we can probably slide the window closed now by moving the gripper right.
    - When the robot's gripper is left of window handle, the robot should slide window right.
    If the gripper is starting to be in front of the window handle, push harder.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

The task `button-press` requires the robot to push the button down.
To push the button down reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button
    The robot needs to line up the gripper from above to press the button.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    When the robot's gripper is lined up from above, push down to press the button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on