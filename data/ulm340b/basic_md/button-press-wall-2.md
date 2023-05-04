
    <<ANS>>

The task `pick-out-of-hole` requires the robot to grab the peg out of the hole.
To grab the peg out of the hole reliably, the robot should perform the following steps:
    - When the peg is not forward aligned with the robot's gripper, the robot should grip peg.
    - When the peg is forward aligned with the robot's gripper and the peg is in hole, the robot should lift peg out of hole.

The task `button-press-side` requires the robot to press the button down from the side.
To press the button down from the side reliably, the robot should perform the following steps:
    - When the button is not horizontally aligned with the robot's gripper and button is not left of the robot's gripper, the robot should grab button.
    - When the button is left of the robot's gripper, the robot should push button down.

The task `pick-out-of-hole-side` requires the robot to grab the peg out of the hole from the side.
To grab the peg out of the hole from the side reliably, the robot should perform the following steps:
    - When the peg is not vertically aligned with the robot's gripper, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the peg is forward aligned with the robot's gripper and the peg is in hole, the robot should lift peg out of hole.

The task `pick-place-behind` requires the robot to pick up the puck behind it and place it to the target location.
To pick up the puck behind it and place it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with puck, the robot should put the gripper above the puck.
    - When the robot's gripper is vertically aligned with puck and the robot's gripper is not near puck, the robot should reach behind robot.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should pick up puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `reach-behind` requires the robot to reach to the target location behind it.
To reach to the target location behind it reliably, the robot should perform the following steps:
    - When the robot's gripper is not above reach goal