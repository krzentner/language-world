
Answer:
    - When the robot's gripper is not vertically aligned with handle, the robot should put gripper above handle.
    - When the robot's gripper is vertically aligned with handle, the robot should push handle down.

The task `pick-out-of-hole` requires the robot to grab the peg and remove it from the hole.
To grab the peg and remove it from the hole reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the peg, the robot should put gripper above peg.
    - When the robot's gripper is not near the peg, the robot should push gripper into peg.
    - When the robot's gripper is near the peg, the robot should pull gripper out of hole.

The task `door-close` requires the robot to push the door close.
To push the door close reliably, the robot should perform the following steps:
    - When the robot's gripper is not near door handle, the robot should grab door handle.
    - When the robot's gripper is vertically aligned with door handle, the robot should push door closed.

The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not near puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is closed, the robot should place puck at goal.

The task `stick-push` requires the robot to push the stick to the right.
To push the stick to the right reliably, the robot should perform the following steps:
    - When the robot's gripper is not near stick and the robot's gripper is open, the robot should put gripper around stick.
    - When the robot's gripper is near stick and the robot's gripper is vertically aligned with stick, the robot should push stick right.

The task `relocate` requires the robot to pick up the puck and move it to the target location.
To pick up the puck and move it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not near puck, the robot should close gripper around puck.
    - When the robot's gripper is around puck and the robot's gripper is near puck, the robot should lift puck above table.
    - When the robot's gripper is above puck and the puck is below the robot's grip