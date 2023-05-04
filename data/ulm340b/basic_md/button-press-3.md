

The task `pick-place-wall` requires the robot to pick up the puck and put it in the wall.
To pick up the puck and put it in the wall reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is around puck and the robot's gripper is not closed, the robot should push the gripper into the puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should put puck in wall.

The task `handle-press` requires the robot to pull the door handle down.
To pull the door handle down reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the door handle, the robot should put gripper above door handle.
    - When the robot's gripper is above the door handle and the robot's gripper is open, the robot should drop gripper around door handle.
    - When the robot's gripper is around door handle, the robot should pull door handle down.

The task `handle-press-topdown` requires the robot to push the door handle down from above.
To push the door handle down from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the door handle, the robot should put gripper above door handle.
    - When the robot's gripper is above the door handle, the robot should push down on door handle.

The task `pick` requires the robot to pick up the puck.
To pick up the puck reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is around puck and the robot's gripper is not closed, the robot should push the gripper into the puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should hold puck in the air.

The task `pick-out-wall` requires the robot to grab the puck out of the wall.
To grab the puck out of the wall reliably, the robot should perform the following steps:
    - When the robot's gripper is not above