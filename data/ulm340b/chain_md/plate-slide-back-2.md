
    Steps:  1. Push plate into goal
    We want to slide the plate back into its target location, so we should just move the robot's gripper towards that goal.
    - When plate is not at goal, the robot should push plate into goal.

The task `pull-lever-back` requires the robot to pull the lever back.
To pull the lever back reliably, what steps the robot should perform?
    Steps:  1. Place gripper above lever handle  2. Close the robot's gripper around the lever handle  3. Pull backwards on lever handle  4. Stop pulling when lever handle is fully pulled
    First, put the gripper above the lever handle, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above lever handle and the robot's gripper is not vertically aligned with lever handle, the robot should put gripper above lever handle.
    If the gripper isn't around the lever handle, put it around the lever handle.
    - When lever handle is not around the robot's gripper and the robot's gripper is open, the robot should close the robot's gripper around the lever handle.
    Now that the gripper is around the lever handle, we can just pull the lever handle.
    - When the robot's gripper is around lever handle, the robot should pull lever handle back.
    When the lever handle reaches the back, we don't have to keep pulling.
    - When lever handle is behind the robot's gripper, the robot should not pull lever handle back.

The task `pull-lever` requires the robot to pull the lever towards the robot.
To pull the lever towards the robot reliably, what steps the robot should perform?
    Steps:  1. Place gripper above lever handle  2. Close the robot's gripper around the lever handle  3. Pull backwards on lever handle
    First, put the gripper above the lever handle, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above lever handle, the robot should put gripper above lever handle.
    If the gripper isn't around the lever handle, put it around the lever handle.
    - When lever handle is not around the robot's gripper and the robot's gripper is open, the robot should close the robot's gripper around the lever handle.
    Now that the gripper is around the lever handle, we can just pull the lever handle.
    - When the robot's gripper is around lever handle,