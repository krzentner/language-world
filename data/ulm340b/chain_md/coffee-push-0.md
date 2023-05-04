
    Steps:  1. Place gripper above mug  2. Push into mug  3. Move mug to goal
    - When the robot's gripper is not above mug, the robot should place gripper above mug.
    - When the robot's gripper is above mug and the robot's gripper is not near mug, the robot should push into mug.
    - When the robot's gripper is near mug and the robot's gripper is open, the robot should close gripper around mug.
    - When the robot's gripper is near mug and the mug is below the robot's gripper, the robot should push mug to goal.

The task `coffee-pull` requires the robot to grab the mug and move it to the target location.
To grab the mug and move it to the target location reliably, what steps the robot should perform?
    Steps:  1. Place gripper above mug  2. Grab mug with gripper  3. Pull mug to goal
    - When the robot's gripper is not above mug, the robot should place gripper above mug.
    - When the robot's gripper is above mug and the robot's gripper is not around mug, the robot should grab mug with gripper.
    - When the robot's gripper is around mug and the robot's gripper is open, the robot should close gripper around mug.
    - When the robot's gripper is around mug, the robot should pull mug to goal.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, what steps the robot should perform?
    Steps:  1. Place gripper in front of button  2. Push button
    - When the robot's gripper is not forward aligned with button, the robot should place gripper in front of button.
    - When the robot's gripper is forward aligned with button and the robot's gripper is open, the robot should close gripper around button.
    - When the robot's gripper is around button and the button is not pushed, the robot should push button.

The task `reach-pick-place` requires the robot to pick up the puck and move it to the target location.
To pick up the puck and move it to the target location reliably, what steps the robot should perform?
    Steps:  1. Place gripper above puck  2. Grab puck with gripper  3. Place puck at goal
    - When the robot's gripper is not above puck, the robot should place gripper above puck.
    - When the