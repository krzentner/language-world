
    Steps:  1. Put gripper above puck  2. Grab puck  3. Move gripper to target location
    To be able to pick up the puck, move the gripper above the puck.
    - When the robot's gripper is not near puck and the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck
    If the puck isn't grabbed and the gripper is aligned with it, try closing the gripper.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the puck
    If the gripper is around the puck, move it to the target location.
    - When the robot's gripper is around the puck, move the robot's gripper until the robot's gripper is near the target location

The task `button-press-side` requires the robot to press the button by pushing on it from the side.
To press the button by pushing on it from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper near the button  2. Push the button down
    If the gripper is not near the button, move it to the button.
    - When the robot's gripper is near the button and the robot's gripper is not forward aligned with the button, move the robot's gripper until the robot's gripper is forward aligned with the button
    If the robot's gripper is aligned with the button, press down on it.
    - When the robot's gripper is forward aligned with the button and the robot's gripper is not near the button, move the robot's gripper until the robot's gripper is near the button and the robot's gripper is closed

The task `push-reach` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal  4. Release gripper
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is