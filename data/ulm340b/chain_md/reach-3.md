
    Steps:  1. Move the gripper to the goal
    The robot can just reach to the target location.
    - When the robot's gripper is not near the goal, the robot should move the robot's gripper to the goal.

The task `lift` requires the robot to grab the handle and lift it up.
To grab the handle and lift it up reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper in front of the handle  2. Close the gripper around the handle  3. Lift up the handle
    Put the gripper in front of the handle.
    - When the robot's gripper is not forward aligned with the handle, the robot should put the gripper in front of the handle.
    Close the gripper around the handle.
    - When the robot's gripper is forward aligned with the handle and the robot's gripper is open, the robot should close the gripper around the handle.
    Lift up the handle.
    - When the robot's gripper is forward aligned with the handle and the robot's gripper is closed, the robot should lift up the handle.

The task `press-side` requires the robot to press on the button sideways.
To press on the button sideways reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper above the button  2. Drop the gripper down to the button
    To move the gripper above the button, check if the gripper is aligned with the button from above.
    - When the robot's gripper is not vertically aligned with the button, the robot should put the gripper above the button.
    Drop the gripper down to the button.
    - When the robot's gripper is vertically aligned with the button and the robot's gripper is open, the robot should drop the gripper down to the button.

The task `push-away` requires the robot to push the target away from itself.
To push the target away from itself reliably, the robot should perform the following steps:
    Steps:  1. Move the gripper roughly in front of the target  2. Move the gripper away from itself
    Move the gripper roughly in front of the target.
    - When the robot's gripper is not near the target, the robot should put the gripper roughly in front of the target.
    Move the gripper away from itself.
    - When the robot's gripper is in front of the target, the robot should move the gripper away from itself.

The task `reach-around` requires the robot to reach around the obstacle to the