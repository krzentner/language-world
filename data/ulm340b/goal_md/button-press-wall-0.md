

The task `toggle-switch-up-down` requires the robot to move the toggle switch from down to up.
To move the toggle switch from down to up reliably, the robot should perform the following steps:
    Steps:  1. Grab the toggle switch from above  2. Flip the switch from the top
    The easiest way to do this is to grab the switch from above and flip it. First, grab the switch from above.
    - When the robot's gripper is not vertically aligned with toggle switch, move the robot's gripper until the robot's gripper is vertically aligned with toggle switch
    Now flip the switch.
    - When the robot's gripper is near toggle switch and the robot's gripper is open, move the robot's gripper until the robot's gripper is left of toggle switch

The task `toggle-switch-down-up` requires the robot to move the toggle switch from up to down.
To move the toggle switch from up to down reliably, the robot should perform the following steps:
    Steps:  1. Grab the toggle switch from below  2. Flip the switch from the bottom
    The easiest way to do this is to grab the switch from below and flip it. First, grab the switch from below.
    - When the robot's gripper is not almost vertically aligned with toggle switch, move the robot's gripper until the robot's gripper is vertically aligned with toggle switch
    Now flip the switch.
    - When the robot's gripper is near toggle switch and the robot's gripper is open, move the robot's gripper until the robot's gripper is right of toggle switch

The task `lever-pull` requires the robot to pull the lever down towards itself.
To pull the lever down towards itself reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above lever  2. Drop gripper around lever  3. Pull lever towards robot
    Put the gripper above lever.
    - When the robot's gripper is not above lever, move the robot's gripper until the robot's gripper is above lever
    Drop the gripper around lever.
    - When the robot's gripper is above lever and the robot's gripper is not around lever, move the robot's gripper until the robot's gripper is around lever
    Pull the lever towards robot.
    - When the robot's gripper is around lever, move the robot's gripper until the robot's gripper is horizontally aligned with lever

The task `light-switch-up-down` requires the robot to flip