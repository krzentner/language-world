
    - The robot should pull drawer handle.
    - The robot should put gripper above drawer handle.
    - The robot should push drawer handle.
    - The robot should place gripper around drawer handle.
    - The robot should push drawer open.
    - The robot should pull drawer open.

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole, the robot should align peg to hole.
    - When peg is vertically aligned with hole, the robot should insert peg into hole.

The task `peg-insert-side-v2` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, what steps the robot should perform?
    - The robot should push door handle.
    - The robot should put gripper above door handle.
    - The robot should push door closed.
    - The robot should place gripper around door handle.
    - The robot should pull door handle.
    - The robot should pull door closed.

The task `button-press-topdown-v2` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `peg