
    - When the robot's gripper is not vertically aligned with peg and the robot's gripper is not left of the peg, the robot should put gripper above peg.
    - When the robot's gripper is left of the peg and the robot's gripper is open, the robot should place gripper around peg.
    - When the robot's gripper is forward aligned with peg, the robot should pull peg out of hole.
    - When the robot's gripper is not near the goal, the robot should put the peg on goal.

The task `insert` requires the robot to grab the peg and insert it into the hole.
To grab the peg and insert it into the hole reliably, what steps the robot should perform?
    - When the robot's gripper is not above peg, the robot should put the robot's gripper above peg.
    - When the robot's gripper is above peg, the robot should pick up peg.
    - When the robot's gripper is not aligned with hole, the robot should move gripper to the hole.
    - When the robot's gripper is forward aligned with hole, the robot should insert peg into hole.

The task `pick-hollow-insertion` requires the robot to pick up the peg and insert it into the hole on the block.
To pick up the peg and insert it into the hole on the block reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with peg, the robot should move gripper above peg.
    - When the robot's gripper is vertically aligned with peg, the robot should pick up peg.
    - When peg is not aligned with block hole and peg is above block, the robot should align peg to block.
    - When the robot's gripper is near block, the robot should put gripper into block.

The task `pick-and-place-with-hollow` requires the robot to pick up the peg and place it at the target location.
To pick up the peg and place it at the target location reliably, what steps the robot should perform?
    - When the robot's gripper is not aligned with peg, the robot should move gripper above peg.
    - When the robot's gripper is vertically aligned with peg, the robot should pick up peg.
    - When the robot's gripper is not near goal, the robot should put the robot's gripper on goal.

The task `align-block-vertical` requires the robot to pick up the block and put it at the target location.
To pick up the block and put it at the target location reliably, what steps the robot should perform?
    - When the robot's grip