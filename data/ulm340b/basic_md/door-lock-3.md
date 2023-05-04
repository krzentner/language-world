
    
    - When the robot's gripper is not near the door dial and the robot's gripper is not vertically aligned with the door dial, the robot should move gripper above the door dial.
    - When the robot's gripper is near the door dial and the robot's gripper is vertically aligned with the door dial, the robot should turn the door dial.

The task `door-close` requires the robot to push the door shut.
To push the door shut reliably, the robot should perform the following steps:
    - When the robot's gripper is not forward aligned with the door handle, the robot should put gripper around door handle.
    - When the robot's gripper is in front of the door handle, the robot should push door.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button and the robot's gripper is not horizontally aligned with the button, the robot should put the gripper above button.
    - When the robot's gripper is horizontally aligned with button and the robot's gripper is open, the robot should put gripper around button.
    - When the robot's gripper is not forward aligned with button, the robot should press button.

The task `block-stack` requires the robot to stack the block on top of the other block.
To stack the block on top of the other block reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with block and the robot's gripper is not below the block, the robot should move the gripper above the block.
    - When the robot's gripper is vertically aligned with the block and the robot's gripper is open, the robot should drop gripper around the block.
    - When the robot's gripper is not near the block and the robot's gripper is open, the robot should close gripper around the block.
    - When the robot's gripper is near the block and the robot's gripper is closed, the robot should lift gripper above the block.
    - When the robot's gripper is near the top block and the robot's gripper is closed, the robot should drop the gripper on top of the top block.

The task `door-unlock` requires the robot to turn the dial on the door.
To turn the dial on the door reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the door dial and the robot's gripper is not vertically