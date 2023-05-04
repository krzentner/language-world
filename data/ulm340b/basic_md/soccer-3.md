
    - When the robot's gripper is not above the soccer ball, the robot should move its gripper above the soccer ball.
    - When the robot's gripper is above the soccer ball and the robot's gripper is not touching the soccer ball, the robot should push the soccer ball to the goal.
    - When the robot's gripper is touching the soccer ball, the robot should push harder.

The task `insert` requires the robot to grab the peg and insert it into the hole.
To insert the peg into the hole reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the peg and the robot's gripper is not open, the robot should move gripper above peg.
    - When the robot's gripper is not below the peg and the robot's gripper is not open, the robot should put gripper below peg.
    - When the robot's gripper is not open, the robot should open gripper.
    - When the robot's gripper is not near the peg, the robot should grab peg.
    - When the robot's gripper is forward aligned with peg and the robot's gripper is not near peg, the robot should pull gripper away from peg.
    - When the robot's gripper is forward aligned with peg and the robot's gripper is near peg, the robot should insert peg into hole.

The task `push-left` requires the robot to push the button left.
To push the button left reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the button, the robot should move the gripper left of button.
    - When the robot's gripper is not below the button, the robot should put the gripper below the button.
    - When the robot's gripper is below the button and the robot's gripper is not touching the button, the robot should push the button to the left.
    - When the robot's gripper is touching the button, the robot should push the button harder.

The task `button-press-side` requires the robot to press the button from the side.
To press the button from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not horizontally aligned with button, the robot should put gripper near button.
    - When the robot's gripper is horizontally aligned with button, the robot should push button side.

The task `door-close` requires the robot to close the door.
To close the door reliably, the robot should perform the following steps:
    - When the robot's gripper is not touching door, the robot