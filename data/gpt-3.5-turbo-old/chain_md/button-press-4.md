The task `button-press` requires the robot to push the button from the front.
To push the button from the front reliably, the robot should perform the following steps:
    Steps:  1. Put gripper in front of the button  2. Push gripper towards the button to press it
    Since this is not "topdown" but "frontal", the gripper needs to be positioned in front of the button instead of above it.
    - When the robot's gripper is not in front of the button, the robot should place gripper in front of button.
    Once the gripper is positioned in front of the button, press the button by pushing the gripper towards it.
    - When the robot's gripper is in front of the button, the robot should push the gripper towards the button to press it.