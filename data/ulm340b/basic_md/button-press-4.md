

Possible answers are:
    - When the robot's gripper is not in front of button, the robot should move gripper to in front of button.
    - When the robot's gripper is in front of button, the robot should push the button down.

Question: When the robot's gripper is not in front of button, the robot should:
Answer: move gripper to in front of button

Question: When the robot's gripper is in front of button, the robot should:
Answer: push the button down


The task `door-close` requires the robot to push the door close.
To push the door close reliably, the robot should perform the following steps:
    - When the robot's gripper is not forward aligned with door handle, the robot should put gripper around door handle.
    - When the robot's gripper is forward aligned with door handle, the robot should push door closed.

The task `peg-unstack` requires the robot to remove the top peg from the stack.
To remove the top peg from the stack reliably, the robot should perform the following steps:
    - When the robot's gripper is not above top peg, the robot should put the gripper above the top peg.
    - When the robot's gripper is above top peg, the robot should pull top peg out of the stack.

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When the robot's gripper is vertically aligned with the peg and the peg is not near the robot's gripper, the robot should push the gripper down into the peg.
    - When peg is near the robot's gripper and peg is not aligned with hole, the robot should align peg to hole.
    - When peg is aligned with hole, the robot should insert peg into hole.

The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot