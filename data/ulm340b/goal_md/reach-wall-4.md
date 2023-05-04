
    Steps:  1. Reach towards the target while making sure the robot does not hit the wall  2. When reaching above the wall, line up the gripper with the target
    We can only reach to the target location with a short wall in the way by either reaching above it, or reaching around it.
    - When the robot's gripper is not above the wall and the robot's gripper is near the wall, move the robot's gripper until the robot's gripper is above the wall and the robot's gripper is near reach target
    If the robot's gripper is above the wall and near the reach target, then we're good. We're doing it.
    - When the robot's gripper is not above the wall and the robot's gripper is left of the wall, move the robot's gripper until the robot's gripper is left of the wall and the robot's gripper is near reach target
    We have to keep the robot's gripper away from the wall to avoid collisions.
    - When the robot's gripper is not near the reach target, move the robot's gripper until the robot's gripper is near the reach target

The task `reach-high` requires the robot to reach to the target location that is high up.
To reach to the target location that is high up reliably, what steps the robot should perform?
    Steps:  1. Reach as high as you can, then put gripper above the target
    If the robot's gripper is below reach target, move up the gripper.
    - When the robot's gripper is below the reach target, move the robot's gripper until the robot's gripper is above the reach target
    If the robot's gripper is near the reach target, then we're good. We're doing it.
    - When the robot's gripper is above the reach target and the robot's gripper is not near the reach target, move the robot's gripper until the robot's gripper is near the reach target

The task `reach-wall-high` requires the robot to reach to the target location that is high up with a short wall in the way.
To reach to the target location that is high up with a short wall in the way reliably, what steps the robot should perform?
    Steps:  1. Reach as high as you can, then put gripper above the wall  2. When above the wall, put gripper above the target and line up with the target
    If the robot's gripper is below wall, move up the gripper.
    -