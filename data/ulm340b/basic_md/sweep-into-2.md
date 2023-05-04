

The task `pick-place-into` requires the robot to grab the puck and move it to the target location.
To grab the puck and move it to the target location reliably, what steps the robot should perform?

The task `push-into` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

The task `sweep-cube-into-goal` requires the robot to grab the cube and slide it to the target location.
To grab the cube and slide it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not around the cube, the robot should put the gripper around the cube.
    - When the robot's gripper is around the cube, the robot should slide the cube to the goal.

The task `sweep-puck-into-goal` requires the robot to grab the puck and slide it to the target location.
To grab the puck and slide it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

The task `sweep-multi-into-goal` requires the robot to grab the cube and slide it to the target location.
To grab the cube and slide it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not around the cube, the robot should put the gripper around the cube.
    - When the robot's gripper is around the cube, the robot should slide the cube to the goal.

The task `push-into-goal` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the