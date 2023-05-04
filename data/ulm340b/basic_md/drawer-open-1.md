

>>> q1 = ['When the robot's gripper is not vertically aligned with the drawer handle, the robot should put gripper above drawer handle.', 'When the robot\'s gripper is vertically aligned with the drawer handle and the robot\'s gripper is open, the robot should put gripper around drawer handle.', 'When the robot\'s gripper is vertically aligned with the drawer handle and the drawer handle is not horizontally aligned with the drawer, the robot should pull drawer open.']


The task `peg-insert-sideway` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the peg, the robot should place gripper above peg.
    - When the robot's gripper is near the peg and the peg is not horizontally aligned with the hole, the robot should align peg to hole.
    - When the peg is horizontally aligned with the hole, the robot should insert peg into hole.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not horizontally aligned with the button, the robot should place gripper next to button.
    - When the robot's gripper is near the button and the robot's gripper is not in front of the button, the robot should push the button.

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When the robot's gripper is near the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the door handle, the robot should put gripper above door handle.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    - When the robot's gripper is vertically aligned with the door handle, the robot