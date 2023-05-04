

The task `pick-place-with-camera` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    We closed the gripper, and the puck is still near the gripper, so maybe we grabbed it. Try to move the puck to the goal. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `door-unlock` requires the robot to turn the dial on the door.
To turn the dial on the door reliably, what steps the robot should perform?

The task `drawer-close-topdown` requires the robot to push the drawer closed.
To push the drawer closed reliably, the robot should perform the following steps:
    Steps:  1. Move gripper roughly above the drawer handle  2. Push drawer closed
    As long as the gripper is above the drawer handle, we should be able to push the drawer closed.
    - When the robot's gripper is not above drawer handle and the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    Now that we've put the gripper above the drawer, we just need to push the drawer closed.
    - When the robot's gripper is above drawer handle, the robot should push drawer closed.

The task `button-press-side` requires the robot to push the button to the side.
To push the button to the side reliably, the robot should perform the following steps:
    Steps:  1.