
    Steps:  1. Line up the robot's gripper as seen from above  2. Push gripper into faucet as seen from above to grasp it  3. Push gripper in opposite direction to turn
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with faucet, the robot should put gripper above faucet.
    Now that the gripper is lined up, just push down on the faucet.
    - When the robot's gripper is vertically aligned with faucet, the robot should push gripper into faucet.
    Now that the gripper is near the faucet, we just have to turn the faucet the other direction.
    - When the robot's gripper is near faucet, the robot should turn faucet handle.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Push gripper into door handle  3. Push the door closed
    If the gripper is not above the door handle, move it above.
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    Now that the gripper is lined up, we just need to make sure it is in front of the door handle
    - When the robot's gripper is almost vertically aligned with door handle and the robot's gripper is not in front of door handle, the robot should put gripper in front of door handle.
    If the robot's gripper is in front of door handle, we can push the door closed.
    - When the robot's gripper is in front of door handle, the robot should push door closed.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the robot's gripper as viewed from the side  2. Slide robot's gripper into button from the side to grasp it  3. Push the button by moving gripper away
    Because this is "side", we just need to line up the gripper from the side. Line up the robot's gripper from the side.
    - When the robot's gripper is not horizontally aligned with button, the robot should put gripper to the side of button.
    Now that the gripper is lined up