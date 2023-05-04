
    - When the robot's gripper is not forward aligned with the stick, the robot should grab the stick.
    - When the robot's gripper is left of the thermos and the robot's gripper is left of the stick, the robot should place the gripper left of the thermos.
    - When the robot's gripper is not near the thermos, the robot should place gripper near thermos.
    - When the robot's gripper is near the thermos and the robot's gripper is not right of the thermos, the robot should push the thermos away from the robot.

The task `stick-push` requires the robot to grab the stick and use it to push the thermos to the target location.
To grab the stick and use it to push the thermos to the target location reliably, what steps the robot should perform?
    - When the robot's gripper is not forward aligned with the stick, the robot should grab the stick.
    - When the robot's gripper is right of the thermos and the robot's gripper is right of the stick, the robot should place the gripper right of the thermos.
    - When the robot's gripper is not near the thermos, the robot should place gripper near thermos.
    - When the robot's gripper is near the thermos and the robot's gripper is not left of the thermos, the robot should push the thermos away from the robot.

The task `thermos-pick` requires the robot to pick up the thermos and move it to the target location.
To pick up the thermos and move it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not forward aligned with the thermos, the robot should place gripper below thermos.
    - When the robot's gripper is below the thermos and the robot's gripper is not around thermos, the robot should place gripper around thermos.
    - When the robot's gripper is below thermos and the robot's gripper is around thermos, the robot should pick up the thermos.
    - When the robot's gripper is above thermos and the robot's gripper is below thermos, the robot should place thermos at goal.

The task `box-pick` requires the robot to pick up the box and move it to the target location.
To pick up the box and move it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the box, the robot should place gripper above box.
    - When the robot's gripper is not