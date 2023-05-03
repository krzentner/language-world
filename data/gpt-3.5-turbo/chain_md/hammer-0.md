The task `hammer` requires the robot to hit the nail with the hammer, to do this reliably, the robot should perform the following steps:
    Steps:  1. Position the hammer above the nail  2. Grab the hammer  3. Raise the hammer  4. Position the hammer above the nail again at an angle  5. Bring the hammer down to hit the nail
    First, position the hammer above the nail so that we don't hit the finger or miss the nail.
    - When the robot's gripper is not above the nail, the robot should put the gripper above the nail.
    Once the gripper is above the nail, we can grab the hammer.
    - When the robot's gripper is above the nail and the robot's gripper is not around the hammer, the robot should grab the hammer.
    After we grabbed the hammer, we need to raise it up to be able to hit the nail.
    - When the robot's gripper is holding the hammer and the hammer is not raised, the robot should raise the hammer.
    Now that the hammer is raised, we need to position it above the nail again at an angle where we can hit it.
    - When the robot's gripper is holding the raised hammer and the hammer is not positioned above the nail at an angle, the robot should position the hammer above the nail again at an angle.
    Finally, we bring the hammer down to hit the nail.
    - When the robot's gripper is holding the hammer above the nail at an angle, the robot should bring the hammer down to hit the nail.