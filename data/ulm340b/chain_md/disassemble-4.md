
    Steps: 1. Put gripper above peg  2. Put gripper around peg  3. Lift the gripper
    First, put the gripper roughly above the peg to be able to grab it.
    - When the robot's gripper is not above peg, the robot should place gripper above peg.
    Put the gripper around the peg to be able to grab it.
    - When the robot's gripper is above peg and the robot's gripper is open, the robot should close gripper around peg.
    Once the gripper is around the peg, we can just pull the gripper upwards.
    - When the robot's gripper is around peg, the robot should lift up gripper.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from the side  2. Push the button with the gripper
    Because this is "side", we just need to line up the gripper from the side. Line up the robot's gripper from the side.
    - When the robot's gripper is not forward aligned with button, the robot should put gripper next to button.
    Now that the gripper is lined up, just push the button.
    - When the robot's gripper is forward aligned with button, the robot should push into button.

The task `block-stack` requires the robot to stack the blocks into a pyramid.
To stack the blocks into a pyramid reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the blue block  2. Drop gripper around blue block  3. Lift up the gripper  4. Place gripper around yellow block  5. Lift up the gripper  6. Place gripper around red block  7. Lift up the gripper
    First, put the gripper above the blue block.
    - When the robot's gripper is not above the blue block, the robot should put gripper above blue block.
    Once the gripper is above the blue block, we can probably grab it by dropping it.
    - When the robot's gripper is above the blue block and the robot's gripper is open, the robot should drop gripper around blue block.
    Once the gripper is around the blue block, we can probably lift the block.
    - When the robot's gripper is around the blue block, the robot should lift gripper up.
    Now