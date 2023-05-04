
    - When the robot's gripper is not vertically aligned with puck and the robot's gripper is not near the wall, the robot should move gripper to above puck.
    - When the robot's gripper is near the puck and the robot's gripper is open, the robot should drop gripper down around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `pick-place-shelf` requires the robot to pick up the puck and hold it at the target location on the shelf.
To pick up the puck and hold it at the target location on the shelf reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with puck and the robot's gripper is not above the shelf, the robot should move gripper to above puck.
    - When the robot's gripper is near the puck and the robot's gripper is open, the robot should drop gripper down around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `push-wall` requires the robot to push the puck around the small wall to the target location.
To push the puck around the small wall to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above puck and the robot's gripper is not above the wall, the robot should move gripper to above puck.
    - When the robot's gripper is near the puck and the puck is not horizontally aligned with wall, the robot should push puck to wall.
    - When the robot's gripper is vertically aligned with puck and the puck is below the robot's gripper, the robot should push puck along wall.
    - When the robot's gripper is below puck and the puck is below wall, the robot should push puck into goal.

The task `rearrange` requires the robot to rearrange the blocks to match the target configuration.
To rearrange the blocks to match the target configuration reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with a block and the robot's gripper is not above a goal, the robot should put gripper above a block.
    - When the robot's gripper is