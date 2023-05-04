
    Steps:  1. Pick up the stick  2. Pull the thermos towards the target location
    First pick up the stick.
    - When the robot's gripper is not above the stick and the robot's gripper is not open, the robot should place gripper above stick.
    - When the robot's gripper is above the stick and the robot's gripper is open, the robot should drop gripper around stick.
    - When the robot's gripper is around the stick and the robot's gripper is open, the robot should close gripper around stick.
    Now pull the thermos towards the target location.
    - When the thermos is not at the target location, the robot should pull thermos towards target.

The task `stick-push` requires the robot to grab the stick and use it to push the thermos to the target location.
To grab the stick and use it to push the thermos to the target location reliably, what steps the robot should perform?
    Steps:  1. Pick up the stick  2. Push the thermos towards the target location
    First pick up the stick.
    - When the robot's gripper is not above the stick and the robot's gripper is not open, the robot should place gripper above stick.
    - When the robot's gripper is above the stick and the robot's gripper is open, the robot should drop gripper around stick.
    - When the robot's gripper is around the stick and the robot's gripper is open, the robot should close gripper around stick.
    Now push the thermos towards the target location.
    - When the thermos is not at the target location, the robot should push thermos towards target.

The task `pick-place-side` requires the robot to pick up the puck and drop it at the target location.
To pick up the puck and drop it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Put puck at goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    If