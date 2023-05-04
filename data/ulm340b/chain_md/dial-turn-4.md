
    First, we need to grab the dial. Place the gripper around the dial.
    - When the robot's gripper is not around the dial, the robot should put gripper around dial.
    As long as the gripper is around the dial, turn it.
    - When the robot's gripper is around the dial, the robot should turn dial.

The task `push-turn` requires the robot to push the door open while turning the dial.
To push the door open while turning the dial reliably, the robot should perform the following steps:
    Steps:  1. Put gripper around dial  2. Turn the dial and door
    First, we need to grab the dial. Place the gripper around the dial.
    - When the robot's gripper is not around the dial, the robot should put gripper around dial.
    As long as the gripper is around the dial, turn it.
    - When the robot's gripper is around the dial, the robot should turn dial.

The task `pick-out-of-hole` requires the robot to pick the peg out of the hole.
To pick the peg out of the hole reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the top of the hole  4. Lift peg up out of the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg, lift the peg out of the hole.
    - When the robot's gripper is forward aligned with peg, the robot should lift peg out of hole.

The task `push-in-hole` requires the robot to push the peg down into the hole.
To push the peg down into the hole reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Push the peg down into the hole
    The robot can slide the peg by trapping it by pushing down on it from above and moving the gripper. If the peg isn't below the gripper as seen from above, move the gripper above the peg.
    - When the robot'