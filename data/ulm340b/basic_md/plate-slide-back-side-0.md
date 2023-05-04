
The robot should perform the following steps:
    - When the plate is in front of the robot's gripper, the robot should grab the plate.
    - When the robot's gripper is around the plate and the plate is in front of the robot's gripper, the robot should slide the plate back.
    - When the robot's gripper is around the plate and the plate is to the left of the robot's gripper, the robot should slide the plate to the right.

The task `plate-slide-side` requires the robot to slide the plate sideways into the target location.
To slide the plate sideways into the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not around the plate, the robot should slide gripper around plate.
    - When the robot's gripper is around the plate and the robot's gripper is not in front of the plate, the robot should slide gripper in front of plate.
    - When the robot's gripper is in front of the plate and the robot's gripper is not at the side of the plate, the robot should slide gripper to the side of the plate.
    - When the robot's gripper is at the side of the plate and the plate is to the left of the robot's gripper, the robot should slide the plate to the right.

The task `peg-insert-side-v2` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?
The robot should perform the following steps:
    - When the peg is not below the robot's gripper and the peg is not horizontally aligned with the robot's gripper, the robot should grab the peg.
    - When the robot's gripper is around the peg and the peg is not horizontally aligned with the robot's gripper, the robot should move the peg above the hole.
    - When the robot's gripper is vertically aligned with the peg and the peg is to the right of the robot's gripper, the robot should insert the peg into the hole.

The task `window-open-side` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, what steps the robot should perform?
The robot should perform the following steps:
    - When the robot's gripper is not around the window handle, the robot should grab the window handle.
    - When the robot's gripper is around the window handle and the window handle is to the right of the robot's gripper, the robot should slide the window left.

