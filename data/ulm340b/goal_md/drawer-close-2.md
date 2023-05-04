
    The robot can perform these steps reliably:    
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Push close the drawer
    We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is vertically aligned with the drawer handle
    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle
    Once the gripper is around the drawer handle, we can just push the drawer closed.
    - When the robot's gripper is around drawer handle, move the robot's gripper until the robot's gripper is horizontally aligned with the drawer handle

The task `button-press` requires the robot to push the button down from the front.
To push the button down from the front reliably, the robot should perform the following steps:
    Steps:  1. Put gripper in front of button  2. Line up the gripper  3. Push down on the button
    If the robot's gripper is not near the button, we should move the gripper towards the button.
    - When the robot's gripper is not near button, move the robot's gripper until the robot's gripper is near the button
    Once the gripper is around the button, we can push it down.
    - When the robot's gripper is near button and the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button
    When the gripper is lined up, push the button.
    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button

The task `push-left` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal
    First, put the gripper above puck, so that we don't bump it while