
    Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

The task `button-press` requires the robot to push the button down from the side.
To push the button down from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper left of button  2. Slide gripper into button  3. Push button
    If the gripper is right of the button, move it to the left of the button.
    - When the button is not left of robot's gripper, the robot should put gripper to left of button.
    If the gripper is left of the button, push it toward the button to start pressing it down.
    - When the button is left of the robot's gripper, the robot should push into button.
    If the button is left and forward of the gripper, it's being pushed down, so keep pushing.
    - When the button is left and forward of robot's gripper, the robot should push button down.

The task `door-toggle-side` requires the robot to flip the switch on the door handle up and down.
To flip the switch on the door handle up and down reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above switch  2. Put gripper around switch  3. Flip switch
    If the robot's gripper is not above the switch, we should move it there.
    - When the robot's gripper is not above the switch, the robot should put gripper above switch.
    If the robot's gripper is above the switch, we should move it around the switch.
    - When the robot's gripper is above the switch and the robot's gripper is open, the robot should put gripper around switch.
    If the robot's gripper is around the switch, we should flip the switch.
    - When the robot's gripper is around the switch, the robot should flip switch.

The task `drawer-toggle-side` requires the robot to flip the switch on the drawer handle up and down.
To flip the switch on the drawer handle up and down reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above switch  2. Put gripper around switch  3. Flip switch
    If the robot's gripper is not above the switch, we should move it there.
    - When the robot's gripper is not above the switch, the robot should put gripper above switch.