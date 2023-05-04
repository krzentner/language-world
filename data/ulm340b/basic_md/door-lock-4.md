
    - When the robot's gripper is not around the door dial, the robot should put gripper around door dial.
    - When the robot's gripper is around the door dial, the robot should turn door dial.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not near door, the robot should push toward door.
    - When the robot's gripper is near door, the robot should push door closed.

The task `pick-place-with-obstacle` requires the robot to pick up the puck and hold it at the target location, with a barrier in the way.
To pick up the puck and hold it at the target location, with a barrier in the way reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the puck and the robot's gripper is in front of the barrier, the robot should reach to barrier.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not above the puck, the robot should put gripper above puck.
    - When the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is around the puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is above the puck and the robot's gripper is closed, the robot should place puck at goal.

The task `button-press-side` requires the robot to press the button from the side.
To press the button from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the button, the robot should put gripper above button.
    - When the robot's gripper is open, the robot should drop gripper around button.
    - When the robot's gripper is closed, the robot should press button.

The task `peg-unplug-side` requires the robot to grab the peg and pull it out of the hole from the side.
To grab the peg and pull it out of the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When the robot's gripper is vertically aligned with the peg and the peg is not near the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg, the robot