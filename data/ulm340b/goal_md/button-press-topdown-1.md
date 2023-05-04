
    Steps:  1. Put gripper right above the button  2. Push down on button with the gripper
    The robot can push the button with its gripper, but the button is hard to move so it might take a long time to press it. First, put the gripper above the button.
    - When the robot's gripper is not above the button, move the robot's gripper until the robot's gripper is above the button
    Once the gripper is above the button, press down.
    - When the robot's gripper is above the button, move the robot's gripper until the robot's gripper is almost above the button and the robot's gripper is closed

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, what steps the robot should perform?
    Steps:  1. Put gripper right of the button  2. Push left on button with the gripper
    The robot can push the button with its gripper, but the button is hard to move so it might take a long time to press it. First, put the gripper right of the button.
    - When the robot's gripper is not right of the button, move the robot's gripper until the robot's gripper is right of the button
    Once the gripper is right of the button, press to the left.
    - When the robot's gripper is right of the button, move the robot's gripper until the robot's gripper is almost right of the button and the robot's gripper is closed

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, move the robot's gripper until the robot's gripper is near the door handle
    If the door is aligned with the gripper as seen from in front, we can push the door closed.
    - When the robot's gripper is forward aligned with door handle, move the robot's gripper until the robot's gripper is around the door handle

The task `peg-insert-topdown` requires the robot to grab the