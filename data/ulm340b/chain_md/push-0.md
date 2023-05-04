
    What steps the robot should perform?

The task `push-side` requires the robot to slide the puck sideways to the target location.
To slide the puck sideways to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper sideways next to the puck  2. Move gripper sideways to push the puck
    The puck is already in a good location, just to the left of the gripper. Move the robot's gripper to the side of the puck.
    - When the robot's gripper is not near puck, the robot should place gripper next to puck.
    The puck is already mostly to the right of the gripper, so pushing against it from the side will hopefully move the puck right.
    - When the robot's gripper is near puck and the puck is not to the right of the robot's gripper, the robot should push puck right.

The task `pull` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper to the side of the puck  2. Pull the puck
    First, line the robot's gripper up to the left of the puck, because this is a "pull" task.
    - When the puck is not left of the robot's gripper, the robot should place gripper left of puck.
    If the puck is above the robot's gripper, we can probably pull it forward by moving the robot's gripper backwards.
    - When the robot's gripper is below puck and the puck is to the left of the robot's gripper, the robot should pull puck forward.

The task `drawer-close-side` requires the robot to push the drawer closed sideways.
To push the drawer closed sideways reliably, the robot should perform the following steps:
    Steps:  1. Put gripper to the right of the drawer handle  2. Push the drawer closed sideways
    If the drawer handle is left of the robot's gripper, we should probably move the robot's gripper closer to the drawer handle, on the right side.
    - When the drawer handle is left of the robot's gripper and the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    If the drawer handle is right of the robot's gripper, we can probably just push it closed from the side.
    - When the drawer handle is right of the robot's gripper, the robot should push drawer closed.

The task `drawer-open-side`