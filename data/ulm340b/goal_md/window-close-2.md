
    Steps:  1. Put gripper in front of the window handle  2. Start pushing against the window handle to close the window
    If the robot's gripper is not in front of the window handle, we should put the gripper there and push the window closed.
    - When the robot's gripper is not near the window handle, move the robot's gripper until the robot's gripper is near the window handle
    Once the gripper is in front of the window handle, the gripper can push the window handle to close the window.
    - When the robot's gripper is in front of the window handle and the robot's gripper is not near the window handle, move the robot's gripper until the robot's gripper is near the window handle

The task `block-pick-place` requires the robot to pick up the block and hold it at the target location.
To pick up the block and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the block  2. Drop gripper around block  3. Grab the block  4. Move block to the goal
    First, put the gripper above the block so that we don't bump the block while trying to grab it.
    - When the robot's gripper is not above the block, move the robot's gripper until the robot's gripper is above the block
    If the gripper isn't near the block, put it around the block.
    - When the robot's gripper is not around block, move the robot's gripper until the robot's gripper is around block and the robot's gripper is closed
    If the gripper is near the block but not closed, it might grab the block when we close it.
    - When the robot's gripper is around block, move the robot's gripper until the robot's gripper is near the target location
    Now that the block is in the gripper, we can just move the robot's gripper to the goal.
    - When the robot's gripper is around the target location, move the robot's gripper until the robot's gripper is above the target location

The task `block-push` requires the robot to push the block to the target location.
To push the block to the target location reliably, what steps the robot should perform?
    Steps:  1. Put the gripper above the block  2. Drop the gripper on top of the block  3. Push the block to the target location
    First, put the