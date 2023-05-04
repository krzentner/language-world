

    - 

    - 


The task `peg-unstack` requires the robot to grasp the top peg from the peg stack.
To grasp the top peg from the peg stack reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the top peg and the robot's gripper is not vertically aligned with the top peg, the robot should put the gripper above the top peg.
    - When the robot's gripper is vertically aligned with the top peg and the robot's gripper is not below the top peg, the robot should push the gripper to the top of the top peg.
    - When the robot's gripper is above the top peg and the robot's gripper is closed, the robot should close the gripper around the top peg.

The task `peg-insert-vertical` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the peg, the robot should put gripper above peg.
    - When the robot's gripper is above the peg and the peg is not below the robot's gripper, the robot should drop gripper around peg.
    - When the robot's gripper is below the peg and the peg is not vertically aligned with hole, the robot should place gripper above hole.
    - When the peg is vertically aligned with hole, the robot should insert peg into hole.

The task `peg-insert-side-only-initial-above` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the peg, the robot should put gripper above peg.
    - When the robot's gripper is above the peg and the peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `door-lock` requires the robot to insert the key and turn the lock.
To insert the key and turn the lock reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the key, the robot should put the gripper above the key.
    - When the robot's gripper is above the key and the key is not below the robot's gripper