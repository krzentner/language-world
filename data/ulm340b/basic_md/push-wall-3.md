
- When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
- When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
- When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

The task `push-back` requires the robot to slide the puck back to the start location.
To slide the puck back to the start location reliably, what steps the robot should perform?
- When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
- When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
- When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck away from goal.

The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location, with a wall in the way.
To pick up the puck and hold it at the target location, with a wall in the way reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `block-push` requires the robot to push the block to the target location.
To push the block to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the block, the robot should put gripper near block.
    - When the robot's gripper is near the block and the robot's gripper is not pushing into the block, the robot should push into the block.
    - When the robot's gripper is pushing into the block, the robot should push the block to the goal.

The task `block-pickup` requires the robot to lift the block up.
To lift the block