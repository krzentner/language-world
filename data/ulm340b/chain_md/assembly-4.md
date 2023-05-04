
    Steps:  1. Put gripper above the wrench  2. Close the gripper on the wrench  3. Move gripper around the peg
    First, put the gripper above the wrench.
    - When the robot's gripper is not above the wrench, the robot should place gripper above wrench.
    Once the gripper is roughly above the wrench, we can just close the gripper on the wrench.
    - When the robot's gripper is above wrench and the robot's gripper is open, the robot should close gripper on wrench.
    Now that we're holding the wrench, we can slide it around the peg.
    - When the robot's gripper is around peg and the robot's gripper is closed, the robot should wrap wrench around peg.

The task `button-press` requires the robot to slide the button to the right.
To slide the button to the right reliably, the robot should perform the following steps:
    Steps:  1. Put gripper right of the button  2. Push right on the button  3. Push the button right harder
    If the robot's gripper is not right of the button, we should move the gripper right of the button to start pushing
    - When the robot's gripper is not right of the button and the robot's gripper is not near the button, the robot should move gripper right of button.
    If the robot's gripper is near the button we can start pushing right on the button.
    - When the robot's gripper is near the button and the robot's gripper is right of the button, the robot should push right on button.
    If the robot's gripper is in front of the button, push harder.
    - When the robot's gripper is in front of the button, the robot should push right on button harder.

The task `cable-insert` requires the robot to put the cable into the slot.
To put the cable into the slot reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the cable  2. Move gripper down to put cable into slot
    First, put the gripper above the cable.
    - When the robot's gripper is not vertically aligned with cable, the robot should place gripper above cable.
    Once the gripper is above the cable, move it down. This will either push the cable into the slot or push the cable down, out of alignment with the gripper.
    - When the cable is not aligned with the robot's gripper from the front and cable is not forward aligned