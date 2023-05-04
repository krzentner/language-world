
    - When the robot's gripper is not vertically aligned with dial, the robot should put gripper above dial.
    - When the robot's gripper is vertically aligned with dial and the robot's gripper is not around dial, the robot should grab dial.
    - When the robot's gripper is around dial, the robot should turn dial.

The task `block-stack` requires the robot to pick up the block and put it on the table.
To pick up the block and put it on the table reliably, what steps the robot should perform?
    - When the robot's gripper is not above the block, the robot should place gripper above block.
    - When the robot's gripper is above the block, the robot should lift block.
    - When the robot's gripper is above the block, the robot should drop block on table.

The task `peg-unplug-side` requires the robot to unplug the peg from the side.
To unplug the peg from the side reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with the peg and the peg is not in the robot's gripper, the robot should put the gripper above the peg.
    - When the robot's gripper is vertically aligned with the peg, the robot should grab peg.
    - When the peg is vertically aligned with the robot's gripper and the robot's gripper is not forward aligned with the peg, the robot should lift peg out of hole.
    - When the robot's gripper is forward aligned with the peg, the robot should put peg down.

The task `drawer-close-side` requires the robot to slide the drawer closed from the side.
To slide the drawer closed from the side reliably, what steps the robot should perform?
    - When the drawer is left of the robot's gripper and the robot's gripper is not near the drawer, the robot should push gripper into the drawer.
    - When the drawer is near the robot's gripper, the robot should slide the drawer to the right.

The task `pick-place-bin` requires the robot to pick up the peg and put it in the bin.
To pick up the peg and put it in the bin reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with the peg and the peg is not in the robot's gripper, the robot should put the gripper above the peg.
    - When the robot's gripper is vertically aligned with the peg, the robot should grab peg.
    - When the peg is vertically aligned with the robot's gripper and the robot's gripper is