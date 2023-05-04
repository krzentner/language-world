
    - When the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button, move the robot's gripper until the robot's gripper is left of the button

The task `button-press-topdown-block` requires the robot to push the button down from above with a large block in the way.
To push the button down from above with a large block in the way reliably, what steps the robot should perform?
    - When the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button, move the robot's gripper until the robot's gripper is left of the button

The task `lever-pull-wall` requires the robot to pull the lever.
To pull the lever reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above lever  2. Drop gripper around lever  3. Pull the lever to the left
    We need to put the gripper above the lever before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with lever, move the robot's gripper until the robot's gripper is vertically aligned with the lever
    Once the gripper is lined up above the lever, we should be able to grab the lever by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever, move the robot's gripper until the robot's gripper is around the lever
    Once the gripper is around the lever, we can just pull the lever.
    - When the robot's gripper is around lever, move the robot's gripper until the robot's gripper is horizontally aligned with lever

The task `lever-pull-wall-far` requires the robot to pull the lever.
To pull the lever reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above lever  2. Drop gripper around lever  3. Pull the lever to the left
    We need to put the gripper above the lever before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with lever, move the robot's gripper until the robot's gripper is vertically aligned with the lever
    Once the gripper is lined up above the lever, we should be able to grab the lever by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with